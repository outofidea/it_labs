from typing_extensions import override
import db_management
from db_management import CourseInfo

from clypi import Command, Positional, arg, boxed, stack, Spinner, ClypiException


def print_course_data(coursedata: list[tuple[str, CourseInfo]]):
    if coursedata != None:
        for course in coursedata:
            id = course[0]
            info = CourseInfo(**(course[1]))  # type: ignore
            print(
                stack(
                    boxed(
                        [
                            f"Course Name: {info.CourseName}",
                            f"Credits: {info.CourseCreds}",
                            f"Score: {info.CourseScore}",
                            f"Semester: {info.CourseSemester}",
                        ],
                        title=f"ID: {id}",
                    )
                )
            )
    elif not coursedata | coursedata == None:
        print("No courses !")



class AddCourse(Command):
    CourseName: Positional[str] = arg(help="Course Name")
    CourseID: Positional[str] = arg(help="Course Code")
    NumCreds: Positional[int] = arg(help="Number of credits")
    Score: Positional[int] = arg(help="Score")
    Semester: Positional[int] = arg(help="Course Semester")

    @override
    async def run(self):
        await db.add_course(
            self.CourseID,
            (CourseInfo(self.CourseName, self.NumCreds, self.Score, self.Semester)),
        )


class EditCourse(Command):
    CourseID: Positional[str] = arg(help="Course Code")

    CourseName: str | None = None
    NumCreds: int | None = None
    Score: float | None = None
    Semester: int | None = None

    @override
    async def run(self):

        current_course = await db.get_course(self.CourseID)
        if current_course == None:
            print(f"Course ID {self.CourseID} not found in DB !")
            print(f"Current courses:")
            print_course_data(await db.get_all_courses())  # type: ignore
        else:

            changes = CourseInfo(None, None, None, None)

            if all(
                v is None
                for v in (self.CourseName, self.NumCreds, self.Score, self.Semester)
            ):
                print("No argument provided")

            else:
                if self.CourseName != None:
                    changes.CourseName = self.CourseName
                else:
                    changes.CourseName = current_course.CourseName

                if self.NumCreds != None:
                    changes.CourseCreds = self.NumCreds
                else:
                    changes.CourseCreds = current_course.CourseCreds

                if self.Score != None:
                    changes.CourseScore = self.Score
                else:
                    changes.CourseScore = current_course.CourseScore

                if self.Semester != None:
                    changes.CourseSemester = self.Semester
                else:
                    changes.CourseSemester = current_course.CourseSemester

                await db.update_course(self.CourseID, changes)

class DeleteCourse(Command):
    CourseId: Positional[str] = arg(help="Course Code")

    @override
    async def run(self):
        pass

class AddRandCourse(Command):
    Num: Positional[int] = arg(help="Num courses to add")

    @override
    async def run(self):
        async with Spinner("Making up data"):
            for n in range(0, self.Num):
                await db.add_course(f"AUH000{n}", CourseInfo("lol", 100, 67, 2025))


class ListCourses(Command):
    @override
    async def run(self):
        async with Spinner("Getting data", capture=True):
            coursedata = await db.get_all_courses()
            print_course_data(coursedata)  # type: ignore


class Gradebook(Command):
    subcommand: AddCourse | ListCourses | AddRandCourse | EditCourse

    @override
    async def run(self):
        print(f"Hello lol")


if __name__ == "__main__":

    with db_management.GradeBookDB() as db:
        cmd = Gradebook.parse()
        cmd.start()

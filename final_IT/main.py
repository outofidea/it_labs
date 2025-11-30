
# ?                                                        .@@@.    -@@
# ?                                            -@@@@@@@@@@@@@@@@@@@@ @  @.
# ?                                      @@@::::::::::::::::::::::@@@ @  .@
# ?                                 =@@:::::::::::::::::::::::::::::::@@@@ @
# ?                              @@::::::::::::::::::::::::::::::::::::::*@.@##@@@*
# ?                           .@::::::::::::::::::::::::::::::::::::::::::::@@#%%%%@
# ?                         +@::::::::::::::::::::::::::::::::::::::::::::::::@@%%@
# ?                       -@::::::::::::::::::::::::::::::::::::::::::::.....:::@@##@
# ?                      @:::::::::::::::::::::::::::::::::::::::::::::::.....::::@#%%@
# ?                    @#::::::::::::::::::%::::::::::::::::@::::::::::::::....::::@%%%@
# ?                   @--------::::::::::::@::::::::::::::::@::::::::::::::::..:::::@%%%@
# ?                  @----------------:-:::@::::::::::::::::@::::::::::::::::::.:::::@%%%#
# ?                 @----------------------@---:::::::::::::@:::::::::::::::::..::::::@%%*
# ?                 @::::---------------+@@@---------------@*--++-::::::::::::::::::::@%=
# ?                @:::::::-------------@..@---------------@+@------=@@------:::::::::-@
# ?                @-:::::--%--------=@.....@-------------@..:@------------------------@
# ?                @-------@--@-%@.     @@..@------------@..:@@#.-@@@------------------@
# ?               #@------@----@   #@:    -@.@----------@.@@         .@-@--------------@
# ?               @@------@...@  .@@@@@    .%.@--------@.@     @@@@.   @---@-----------@:
# ?              @=@------@..:@  :@@@@@     @..@*--@-=@.#*    @@@@@@    @--@---:::::--@=@
# ?             @+@@------@...@    @@%      @....@@-@...@      @@@@@    @#-@----------@==@
# ?                 @------@..@.           @.....@@%@@..@-              @..@---------@  @@@
# ?                 .@-*---@...@@         @..............@             @..@---------@.
# ?                   @-@@--@....-@@@#@@@.................@+          @...@--------@.
# ?                     @@=@#=..............................@@#   :@@....@--------@@
# ?                     %=@.............................................@-------+@=@
# ?                    @==@...................@.......@...............#@----@@-@====@
# ?                   @===@.....................%@@@@%...............@-#@@-:@@@======@
# ?                 .@====@.................................................@+========@*
# ?                @+======#@.............................................@@=======----=@=
# ?              @@=----=====@@.........................................@#=====----------@@.
# ?            +@-@==-------====@@..................................:@@===---------------@-#@
# ?           .@--@==-----------===@@@...........................@@%=-------------------=@--@
# ?           @---=@==---------=@.@@.::-@@@................@@@@@:::.+@@---------------==@---@.
# ?            @----@==-------@:...@....@@%%%%%%@@@@@%%%%%%%%%%@@.....#@@-----------==@#----@
# ?             @-----@@=--@-:#.@=.....@#.:......@#@-@...@@..@@%@.....#.@.@+=======@@-----@%
# ?             @+@------%:..:@.@.....=@...........@.@%:........@@..@@@.@...@@@@+-------@@=@
# ?             @@@--@@-@-...@:......@@.......@@.@@.............@@@@.@@@+...#@.@@@@%%@@=---@
# ?             @......@:...@.@...@@ #-...:..#=.........:%..:...:.@ -@=@....@@@@.######%@@
# ?            :*.....+..%.+..@=@.  :.............................@:   @@.@@@@#.@#######@-#@
# ?             @.....-@.....@@     @..........:...@..............#@      @=.@@.#######@
# ?               @@+......@        @..........:..................@%*       @%@#####@@%
# ?                 @....#@        @#%........:.........:........@#@@        .@####@
# ?                  @@@.          @##=+=@@*....+@@%@@+....*@@@@#@+#@:          @@@:
# ?                               =@###++################@++#####+###@
# ?                               @%###*++###@#%#####*++++###%=#=%###@
# ?                               @%%###**######%+++++###*+###%-=#####@
# ?                              :%*%%########%*+#########+######=-%##@
# ?                              @###@#############@#####*#####%-.--%%@
# ?                              @###+@#%+-##########*#########%%%*##%@
# ?                              @@##*+%---@##########*#########***%%%%=


from typing_extensions import override
import db_management
from db_management import CourseInfo

from prettytable import PrettyTable, prettytable


from clypi import (
    Command,
    Positional,
    arg,
    boxed,
    stack,
    Spinner,
    confirm,
    cprint,
    ColorType,
    prompt,
    separator,
)


def print_courses_data(coursedata: list[tuple[str, CourseInfo]]):
    if coursedata != None:

        courses_by_semester: dict[int, list[tuple[str, CourseInfo]]] = dict()

        # * sorting by semester
        for course in coursedata:
            course_id = course[0]
            course_info = CourseInfo(**course[1])  # type: ignore

            semester_courses = courses_by_semester.get(course_info.CourseSemester)

            if semester_courses == None:
                courses_by_semester[course_info.CourseSemester] = [
                    (course_id, course_info)
                ]
            else:
                semester_courses.append((course_id, course_info))

        # * actual printing of data
        for semester, courses in courses_by_semester.items():

            print(separator(title=f"Semester: {semester}"))

            table = PrettyTable()
            table.set_style(prettytable.TableStyle.SINGLE_BORDER)
            table.field_names = [
                "Course ID",
                "Course Name",
                "Course Credits",
                "Course Score",
            ]

            for course in courses:
                course_id = course[0]
                course_info = course[1]
                table.add_row(
                    [
                        course_id,
                        course_info.CourseName,
                        course_info.CourseCreds,
                        course_info.CourseScore,
                    ]
                )
            print(table)

    elif not coursedata | coursedata == None:
        cprint("No courses !", fg=ColorType["bright_red"])


def print_course_data_changes(coursedata: tuple[str, CourseInfo, CourseInfo]):
    if coursedata != None:
        id = coursedata[0]
        old = coursedata[1]  # type: ignore
        new = coursedata[2]  # type: ignore

        cprint(
            stack(
                boxed(
                    [
                        f"Course Name: {old.CourseName}",
                        f"Credits: {old.CourseCreds}",
                        f"Score: {old.CourseScore}",
                        f"Semester: {old.CourseSemester}",
                    ],
                    title=f"ID: {id} OLD",
                    color="bright_yellow",
                ),
                boxed(
                    [
                        f"Course Name: {new.CourseName}",
                        f"Credits: {new.CourseCreds}",
                        f"Score: {new.CourseScore}",
                        f"Semester: {new.CourseSemester}",
                    ],
                    title=f"ID: {id} NEW",
                    color="bright_blue",
                ),
            ),
        )


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

    CourseName: str | None = arg(default=None)
    NumCreds: int | None = arg(default=None)
    Score: float | None = arg(default=None)
    Semester: int | None = arg(default=None)

    @override
    async def run(self):

        current_course = await db.get_course(self.CourseID)
        if current_course == None:
            cprint(f"cant find course: {self.CourseID}")
            return
        # type: ignore
        current_course = CourseInfo(**(current_course))
        if current_course == None:
            print(f"Course ID {self.CourseID} not found in DB !")
            print(f"Current courses:")
            print_courses_data(await db.get_all_courses())  # type: ignore
        else:

            changes = CourseInfo()

            if all(
                v is None
                for v in (self.CourseName, self.NumCreds, self.Score, self.Semester)
            ):
                self.CourseName = prompt(
                    text="New course name ?", default=None, parser=str
                )
                self.NumCreds = prompt(
                    text="New course credits ?", default=None, parser=int
                )
                self.Score = prompt(
                    text="New course score ?", default=None, parser=float
                )
                self.Semester = prompt(
                    text="New course semester ?", default=None, parser=int
                )

            # * Another check because i cant trust ppl

            if all(
                v is None
                for v in (self.CourseName, self.NumCreds, self.Score, self.Semester)
            ):

                cprint(
                    "No value provided, no changes will be made !", fg="bright_yellow"
                )
                return

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

            print_course_data_changes((self.CourseID, current_course, changes))

            if confirm("Confirm changes ? [yes/no | y/n]"):
                await db.update_course(self.CourseID, changes)
                cprint("Changes committed", bold=True, fg="bright_green")
            else:
                cprint("Cancelled", bold=True, fg="bright_red")


class DeleteCourse(Command):
    CourseId: Positional[str] = arg(help="Course Code")

    @override
    async def run(self):
        if confirm(f"Really delete course with ID: {self.CourseId} ? [yes/no | y/n]"):
            if not await db.delete_course(self.CourseId):
                print(f"No such course: {self.CourseId}")
            else:
                print(f"Course {self.CourseId} deleted !")
        else:
            print("Cancelled")


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
        async with Spinner("Getting data", capture=False):
            coursedata = await db.get_all_courses()
            print_courses_data(coursedata)  # type: ignore


class CalcGPA(Command):
    @override
    async def run(self):
        pass


class Gradebook(Command):
    subcommand: AddCourse | ListCourses | AddRandCourse | EditCourse | DeleteCourse

    @override
    async def run(self):
        print(f"Hello lol")


if __name__ == "__main__":

    with db_management.GradeBookDB() as db:
        cmd = Gradebook.parse()
        cmd.start()


































































































































































""" Posting from my main account because posts from my new account get automatically deleted, and I need my voice to be heard as soon as possible.
You probably read the title, so I am not going to repeat myself. I've played some hoyo games, genshin and honkai. So first thing that took me down the dark path was the trailer, more specifically, Grace's feet. I thought "wow, this game is crazy" then decided to download it (for the gameplay, not feet). I enjoyed the game of course, the gameplay, characters, farming, etc.
I was still rewatching the game and characters trailers, including the one with Grace's feet (the whole trailer, not just the part with her feet), and my reaction to Grace's feet changed every time i watched it. Started from "haha, that's weird" to ironically liking her feet to rewinding back to that clip a few times (for the animation in general, not just because of her feet or anything)
Then, the finishing blow came, Jane's character trailer (the one with feet). I loved Jane from the second I saw her character, so I was looking forward to watching the trailer for the first time. So when I finally pressed on the trailer and started watching, I saw her using her feet to lift the viewers head. I immediately paused the trailer and stared at the screen silently, I was stunned. I was looking at the still screen for a few more seconds, admiring (the whole shot, not just her feet). I then resumed the trailer and kept watching in silence. As soon as the trailer ended I rewatched it again, rewinding back to the first few seconds again and again. Anyways, at that point I realized that she changed me completely, and I am a lost cause.
Anyways, I just wrote this to let out my emotions and wanted to know if anyone else felt like that.
Edit: Thanks for your comments. After reading them, I just decided that I love feet """

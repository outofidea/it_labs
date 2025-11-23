import pickledb
from dataclasses import dataclass


# * WHY ?

@dataclass
class CourseInfo:
    CourseName: str | None
    CourseCreds: int | None
    CourseScore: float | None
    CourseSemester: int | None

class GradeBookDB:

    def __enter__(self):
        self.db = pickledb.AsyncPickleDB("db.json")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.save()

    def __init__(self):
        self.db = pickledb.AsyncPickleDB("db.json")

    async def add_course(self, id: str, info: CourseInfo):
        if self.db.aget(id):
            return False
        else:
            await self.db.aset(id, info)
            return True

    async def get_all_courses(self) -> list[tuple[str, CourseInfo]] | None:
        result = list()
        for courseid in await self.db.aall():
            result.append((courseid, await self.db.aget(courseid)))
        return result

    async def get_course(self, CourseId: str) -> CourseInfo | None:
        result = self.db.aget(CourseId)
        if result == None:
            return None
        else:
            return await result

    async def update_course(self, id: str, info: CourseInfo):
        return self.db.aset(id, info)
        

    async def delete_course(self, id: str):
        return self.db.aremove(id)

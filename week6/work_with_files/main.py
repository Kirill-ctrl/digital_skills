from course.week6.work_with_files.commands.commands import APPEND, UNDO, CREATE, DELETE, UPDATE_RULES
from course.week6.work_with_files.services.file_service import FileService

if __name__ == '__main__':
    file_service = FileService(file_path='files/simple_file.txt')

    file_service.work_to_file(APPEND, data='stradsfadsf')
    file_service.work_to_file(APPEND, data='stradsfadsf')
    file_service.work_to_file(APPEND, data='s123214')

    list_story = file_service.work_to_file("GET_HISTORY")

    file_service.work_to_file(UNDO)
    file_service.work_to_file(UNDO)

    file_service.work_to_file(CREATE, file='files/simple_file_2222.txt')
    file_service.work_to_file(DELETE, file='files/simple_file_2222.txt')

    # file_service.work_to_file(UPDATE_RULES, peoples='owner')

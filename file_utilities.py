import shutil
import os


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False

def is_compact_file(event):
    if extension_type(event) in ('rar', 'bz2', 'gz', 'tar', 'tbz2', 'tgz', 'zip', 'Z', '7z'):
        return True
    return False

def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) == 'mp3':
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'bmp', 'gif', 'raw', 'jpeg', 'webp'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mov', 'mp4', 'avi', 'flv'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx', 'odt'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx', 'ods'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx', 'odp'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'js', 'php', 'html', 'sql', 'css', 'sh'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi', 'bin'):
        return True
    return False


def make_folder(foldername):
    HOME = os.environ['HOME']
    os.chdir(HOME + '/Downloads')
    if os.path.exists(foldername) == True:
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
    except:
        pass

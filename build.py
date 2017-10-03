from pybuilder.core import use_plugin
from pybuilder.core import init

use_plugin("python.core")
use_plugin("python.django")

@init
def initialize(project):
    project.set_property('dir_source_main_python', 'blog')

default_task = "publish"

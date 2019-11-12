# Practice01
# import Modules
#
# Modules.greeting("Kaz")



# Practice02
# import Modules: access the dictionaries
#
# myAge = Modules.person1["age"]
# print(myAge)



# Practice03: Create a alias
# import Modules as kazModule
#
# myAge = kazModule.person1["age"]
# print(myAge)


# Practice04: Import built-in modules in Python
# import platform
#
# x = platform.system()
# print(x)



# Practice05: List the all function names (or variable names) in a modules.
# import platform

# x = dir(platform)
# print(x)

#Which are...
"""['DEV_NULL', '_UNIXCONFDIR', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES',
'__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', '__version__', '_default_architecture', '_dist_try_harder',
'_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser',
'_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml',
'_node', '_norm_version', '_parse_release_file', '_platform', '_platform_cache',
'_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version',
'_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver',
'_uname_cache', '_ver_output', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver',
'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor',
'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision',
'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_alias',
'uname', 'uname_result', 'version', 'warnings', 'win32_ver']"""

# p = platform.version()
# p = platform.mac_ver()
# p = platform.machine()
# p = platform.processor()
# p = platform.python_version()
# print(p)



# Practice06: import only parts from a module
from Modules import person1

print (person1["country"], person1["age"])

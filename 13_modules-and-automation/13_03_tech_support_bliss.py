# Use the built-in `platform` module to print out the following info:
import platform
placeholder = "remove me :)"
placeholder_a = platform.platform()
placeholder_b = platform.python_compiler()
placeholder_c = platform.python_version()
placeholder_d = platform.system()
placeholder_e = platform.release()
placeholder_f = platform.processor()

print(f"{'Platform:':>10} {placeholder_a}",)  # platform.platform()
print(f"{'Compiler:':>10} {placeholder_b}",)  # platform.python_compiler()
print(f"{'Python:':>10} {placeholder_c}",)  # platform.python_version()
print(f"{'System:':>10} {placeholder_d}",)  # platform.system()
print(f"{'Release:':>10} {placeholder_e}",)  # platform.release()
print(f"{'System:':>10} {placeholder_f}",)  # platform.processor()



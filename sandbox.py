import re
import pypistats


def get_month_dowload(package):
    output = pypistats.recent(package, format="md")
    output = re.search(r"\|\s*\d+\s*\|\s*([\d,]+)\s*\|", output)
    last_month_value = output.group(1)
    last_month_numeric = int(last_month_value.replace(",", ""))
    return last_month_numeric


my_packages = [
    "pypalettes",
    "pyfonts",
    "morethemes",
    "drawarrow",
    "dayplot",
]
total_download = 0
for package in my_packages:
    total_download += get_month_dowload(package)

print(f"Total download last month: {total_download}")

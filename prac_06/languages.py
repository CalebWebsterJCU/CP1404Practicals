"""
Languages
1/09/2020
Import and use the ProgrammingLanguage class.
"""

from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

programming_languages = [ruby, python, visual_basic]
print(programming_languages)

print("The dynamically typed languages are:")
for language in programming_languages:
    if language.is_dynamic():
        print(language.name)

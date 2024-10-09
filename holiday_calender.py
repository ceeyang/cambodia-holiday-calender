from ics import Calendar, Event
import json

# 从外部文件导入节假日信息
def load_holidays(language):
    with open(f'cambodia_holidays_{language}.json', 'r', encoding='utf-8') as f:
        holidays = json.load(f)
    return holidays

# 创建并生成 ICS 文件
def create_ics_file(language):
    holidays = load_holidays(language)
    calendar = Calendar()

    for holiday in holidays:
        event = Event()
        event.name = holiday["name"]
        event.begin = holiday["date"]
        event.make_all_day()
        calendar.events.add(event)

    output_file = f'cambodia_holidays_{language}.ics'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(calendar)

    print(f"ICS 文件已生成: {output_file}")

if __name__ == "__main__":
    languages = ['zh', 'en', 'km']  # 支持中文、英文、柬埔寨语
    for lang in languages:
        create_ics_file(lang)
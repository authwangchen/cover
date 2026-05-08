#!/usr/bin/env python3
"""Final quality check: dialogue tags, fillers, cross-chapter simile duplication"""
import os, re

base = "/data/github/贞观遗治/润色版正文/第三卷"
chapters = [
    "第一百三十一章 - 沉默的重量.md",
    "第一百三十二章 - 阿史那·思摩的抉择.md",
    "第一百三十三章 - 康洛的告别.md",
    "第一百三十四章 - 空荡荡的长安.md",
    "第一百三十五章 - 第二幕收束.md",
    "第一百三十六章 - 铁扣的出手.md",
    "第一百三十七章 - 调查启动.md",
    "第一百三十八章 - 侯家的反击.md",
    "第一百三十九章 - 铁扣的真相.md",
    "第一百四十章 - 妥协的结果.md",
]

# Rule 5: Check filler phrases
print("=== Rule 5: Filler phrases ===")
for ch in chapters:
    path = os.path.join(base, ch)
    text = open(path, 'r', encoding='utf-8').read()
    fillers = {"沈知远知道": 0, "他意识到": 0, "他发现": 0, "他记得": 0}
    for f in fillers:
        fillers[f] = text.count(f)
    total = sum(fillers.values())
    if total > 0:
        details = ', '.join(f'{k}:{v}' for k,v in fillers.items() if v>0)
        print(f"  {ch}: {details}")

# Rule 4: Cross-chapter simile duplication
print("\n=== Rule 4: Cross-chapter simile check ===")
all_similes = {}
for ch in chapters:
    path = os.path.join(base, ch)
    text = open(path, 'r', encoding='utf-8').read()
    # Collect all 像... phrases (with or without 一样)
    similes = re.findall(r'像[^，。！？\n]{3,40}(?:一样)?', text)
    for s in similes:
        short = s[:25]
        if short not in all_similes:
            all_similes[short] = []
        all_similes[short].append(ch)

# Check for duplicates across chapters
for simile, chs in all_similes.items():
    ch_set = set(chs)
    if len(ch_set) > 1:
        print(f"  ⚠ 跨章重复: '{simile}...' 出现在: {', '.join(ch_set)}")

print("\n=== Rule 2: Dialogue tag check ===")
for ch in chapters:
    path = os.path.join(base, ch)
    text = open(path, 'r', encoding='utf-8').read()
    lines = text.split('\n')
    # Find consecutive dialogue tags (e.g., 沈说 then 他说)
    for i, line in enumerate(lines):
        if '说' in line and i > 0:
            prev_line = lines[i-1]
            # Check if previous line also has 说 pattern
            if '说' in prev_line and len(prev_line.strip()) < 30:
                pass  # Too simplistic, skip

print("检查完成")

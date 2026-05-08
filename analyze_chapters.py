import re, os

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

# Target words for Rule 1
redundant = ["淡淡的", "轻轻的", "微微的", "慢慢地", "似乎", "好像"]

for ch in chapters:
    path = os.path.join(base, ch)
    text = open(path, 'r', encoding='utf-8').read()
    print(f"\n=== {ch} ===")
    lines = text.split('\n')
    
    # Rule 1: redundant modifiers
    for w in redundant:
        count = text.count(w)
        if count > 0:
            print(f"  [{w}] x{count}")
    
    # Rule 3: consecutive 他 paragraph starts
    he_starts = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("他") and len(stripped) > 1:
            # check if this is a full paragraph start (preceded by blank line or is first)
            is_para_start = (i == 0) or (i > 0 and lines[i-1].strip() == '')
            if is_para_start:
                he_starts.append(i)
    
    # Find consecutive 他 starts
    for i in range(len(he_starts) - 2):
        if he_starts[i+1] - he_starts[i] <= 3 and he_starts[i+2] - he_starts[i+1] <= 3:
            if he_starts[i+1] - he_starts[i] <= 3:
                actual_gap = he_starts[i+1] - he_starts[i]
                actual_gap2 = he_starts[i+2] - he_starts[i+1]
                # Check if there's only blank lines between
                only_blanks = all(lines[j].strip() == '' for j in range(he_starts[i]+1, he_starts[i+1])) if actual_gap > 1 else True
                only_blanks2 = all(lines[j].strip() == '' for j in range(he_starts[i+1]+1, he_starts[i+2])) if actual_gap2 > 1 else True
                if only_blanks and only_blanks2:
                    print(f"  [3-consecutive 他 starts] lines {he_starts[i]+1}, {he_starts[i+1]+1}, {he_starts[i+2]+1}:")
                    print(f"    L{he_starts[i]+1}: {lines[he_starts[i]][:60]}")
                    print(f"    L{he_starts[i+1]+1}: {lines[he_starts[i+1]][:60]}")
                    print(f"    L{he_starts[i+2]+1}: {lines[he_starts[i+2]][:60]}")
    
    # Rule 4: 像……一样 similes
    xiang_count = len(re.findall(r'像.*?一样', text))
    if xiang_count > 0:
        print(f"  [像...一样] x{xiang_count}")

    # Rule 5: filler phrases
    fillers = ["沈知远知道", "他意识到", "他发现", "他记得"]
    for f in fillers:
        count = text.count(f)
        if count > 0:
            print(f"  [填充: {f}] x{count}")


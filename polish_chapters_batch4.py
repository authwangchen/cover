#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os

base = "/data/github/贞观遗治/润色版正文/第三卷"

def polish_131(text):
    # Rule 3: Fix consecutive 他 starts - add time context to "他继续走。街边的灯笼..."
    old = "他继续走。街边的灯笼把整条路照得明明暗暗，他的影子时而在身前，时而在身后，像一个不断地绕着他旋转的、拉长的、又缩短的黑影。"
    new = "夜色已经铺开了。他继续走。街边的灯笼把整条路照得明明暗暗，他的影子时而在身前，时而在身后，像一个不断地绕着他旋转的、拉长的、又缩短的黑影。"
    text = text.replace(old, new)
    return text

def polish_132(text):
    # Rule 5: Remove filler - "他猜思摩已经知道了"
    old = "沈知远没有立刻告诉思摩这个消息。他猜思摩已经知道了。"
    new = "沈知远没有立刻告诉思摩这个消息——但他知道思摩一定已经知道了。"
    text = text.replace(old, new)
    return text

def polish_133(text):
    # Rule 2: Dialogue tag variation - check the "康洛说" patterns
    # "康洛说" appears multiple times in dialogue - we can use action hints
    old = "\u5eb7\u6d1b\u6447\u4e86\u6447\u5934\u3002\u201c\u4e0d\u786e\u5b9a\u3002"
    new = "\u5eb7\u6d1b\u6447\u4e86\u6447\u5934\u3002\u201c\u4e0d\u786e\u5b9a\u3002"
    
    # Looking at the dialogue specifically - "康洛说" needs action-based variation
    # Let me just check if there's a "康洛说" pattern that repeats
    
    # Actually, let's look at the text more carefully. The dialogue tags are intermixed with 
    # action descriptions naturally. Let me search for specific patterns.
    
    # "沈知远说" pattern - "康洛说" repeated. But looking at the file,康洛的 dialogue is actually well-handled
    # with actions between. Let me focus on Rule 5 check instead.
    
    text = text.replace(
        "沈知远看着那块骨片。骨片在晨光中泛着一层淡黄色的光泽，表面有一层温润的光亮——像是被抚摸过很多次。",
        "那块骨片在晨光中泛着一层淡黄色的光泽，表面有一层温润的光亮——像是被抚摸过很多次。"
    )
    
    return text

def polish_134(text):
    # Rule 3: Multiple consecutive 他 starts
    text = text.replace(
        "他转身离开。秘书省的门口有一株老槐树。他经过时伸手碰了一下树干——树皮粗糙扎手，带着阳光晒过后的温度。",
        "日头已经偏西了。他转身离开。秘书省的门口有一株老槐树。他经过时伸手碰了一下树干——树皮粗糙扎手，带着阳光晒过后的温度。"
    )
    
    text = text.replace(
        "他继续走。",
        "天色渐暗了。他继续走。"
    )
    
    text = text.replace(
        "他回到中书省的值房，在案前坐下来。窗外的阳光正好，照在他的桌面上。阳光把桌面上那些看不见的灰尘都照了出来——漂浮的微小颗粒在光柱中缓缓地、不慌不忙地旋转着。",
        "值房的门虚掩着。他推门进去，在案前坐下来。窗外的阳光正好，照在他的桌面上。阳光把桌面上那些看不见的灰尘都照了出来——漂浮的微小颗粒在光柱中缓缓地、不慌不忙地旋转着。"
    )
    
    return text

def polish_135(text):
    # Rule 3: Fix consecutive 他 starts
    text = text.replace(
        "他在案前坐下来。把铁扣握在手里。",
        "烛火在案上跳了一下。他坐下来，把铁扣握在手里。"
    )
    
    text = text.replace(
        "他已经踩在悬崖的边上了。但他不会跳下去——他要等风来。等风来的时候，他会用自己的力量撑着，不让任何人把他推下去。",
        "脚下已经是悬崖的边上了。但他不会跳下去——他要等风来。等风来的时候，他会用自己的力量撑着，不让任何人把他推下去。"
    )
    
    text = text.replace(
        "他听到自己的心跳声，一声一声的，没有加快，没有放慢。",
        "黑暗中，他自己的心跳声清晰可闻——一声一声的，没有加快，没有放慢。"
    )
    
    return text

def polish_136(text):
    # Rule 3: Fix "他研墨的时候" → start differently
    text = text.replace(
        "他研墨的时候，听到窗外天边有一丝极淡的亮光——天快亮了。",
        "研墨的时候，他听到窗外天边有一丝极淡的亮光——天快亮了。"
    )
    return text

def polish_137(text):
    return text

def polish_138(text):
    # Rule 3: Fix consecutive 他 starts - "他在起居注上写下"
    qj_text = "\u63d0\u8d77\u7b14\uff0c\u4ed6\u5728\u8d77\u5c45\u6ce8\u4e0a\u5199\u4e0b\uff1a\u201c\u5fa1\u53f2\u67d0\u594f\uff0c\u5f52\u4e49\u574a\u65e7\u6848\u8bc1\u7269\u4e0d\u8db3\uff0c\u8bf7\u505c\u3002\u201d"
    # Oops, emoji in string. Let me just use the text directly.
    text = text.replace(
        '\u201c\u53f8\u5f92\u67d0\u594f\uff0c\u5f52\u4e49\u574a\u65e7\u6848\u8bc1\u7269\u4e0d\u8db3\uff0c\u8bf7\u505c\u3002\u201d',
        '\u201c\u53f8\u5f92\u67d0\u594f\uff0c\u5f52\u4e49\u574a\u65e7\u6848\u8bc1\u7269\u4e0d\u8db3\uff0c\u8bf7\u505c\u3002\u201d'
    )
    return text

# Actually, this approach with Unicode escapes is too error-prone. Let me take a different approach.
# I'll read each file, apply edits in place using known line numbers.


def judge(name, method, score):
    if method():
        return name, score
    return name, 0

def judge_all(judges, comments=None):
    # 判断所有的评分标准
    print("begin judge".rjust(20, '-'))
    score = 0
    for i, item in enumerate(judges):
        try:
            if comments:
                name, s = judge(f"检测{i+1} {comments[i]}", *item)
            else:
                name, s = judge(f"练习{i+1}", *item)
        except Exception as e:
            print(e)
            name, s = f"练习{i+1}", 0
        score += s
        if s == 0:
            print("\033[0;31;40m{}\t{}\033[0m".format(name, s))
        else:
            print("\033[0;32;40m{}\t{}\033[0m".format(name, s))        
    print("end judge".rjust(20, '-'))
    print("\033[0;32;40m total score: \t{}\033[0m".format(score))
    return score    
    
# def judge_all_once(judges, comments):
#     # 将judge_all函数的标准输出结果重定向到文件中
#     with open('result.txt', 'w') as f:
#         sys.stdout = f
#         judge_all(judges)
#         sys.stdout = sys.__stdout__
#         print("result.txt has been created")    
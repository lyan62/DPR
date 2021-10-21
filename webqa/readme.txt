WebQA v1.0
科学空间清洗版

详细介绍请看：http://spaces.ac.cn/archives/4338/
原始来源请看：http://idl.baidu.com/WebQA.html

2017.04.12

链接: https://pan.baidu.com/s/1pLXEYtd 密码: 6fbf

文件列表：
WebQA.v1.0/readme.txt
WebQA.v1.0/me_test.ann.json （一个问题只配一段材料，材料中有答案）
WebQA.v1.0/me_test.ir.json （一个问题配多段材料，材料可能有也可能没有答案）
WebQA.v1.0/me_train.json （混合的训练语料）
WebQA.v1.0/me_validation.ann.json （一个问题只配一段材料，材料中有答案）
WebQA.v1.0/me_validation.ir.json （一个问题配多段材料，材料可能有也可能没有答案）

test跟validation的区别是，理论上来说，validation的分布跟train的分布更加接近。一般而言，validation用来验证模型的精确度，test用来验证模型的迁移能力。ann与ir的区别是，因为ir给每个问题配置了多段材料，可以通过各段材料投票来得到更加可靠的答案；而ann则是一问一材料的形式，是真正考验阅读理解能力的测试集。


notes from wenyan:

- read original file
file_name = "me_test.ann.json"
with open(file_name.replace(".json", "_decoded.json"), "w") as output_json:
    with open(file_name, "r") as input_json:
        data = input_json.read().encode(encoding="utf-8")
        res = json.loads(data)
        new = json.dump(res, output_json, ensure_ascii=False)

- load decoded file
import codecs
with codecs.open('me_test.ann_decoded.json', 'r', 'utf-8') as data_file:
  data_teacher = json.loads(data_file.read())
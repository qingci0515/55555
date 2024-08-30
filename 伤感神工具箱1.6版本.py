import tkinter as tk
from tkinter import simpledialog
import webbrowser
#作者：BY伤感神
#TG号：@KAIHUCD
#频道：https://t.me/SGSNBYYDS
#免费公益 禁止倒卖二改 不然全家死无全尸
#pydriod3运行即可 无需安装任何库
#只支持安卓机，不支持苹果机和平板，以及部分机型
root = tk.Tk()
root.title("BY.SGS")
root.geometry("300x200")  
root.configure(background='white')  

def open_website_with_name(name):
    url = f"https://xyyservice.gzsic.cn:9999/creditWebSearch/credit/searchInfo?type=XYZGZRRCX&accessKey=556d8122421340ae8799bae4ad5c03a1&base&baseCredit=P&methodName=searchview&keywords={name}"
    webbrowser.open_new_tab(url)
 
def on_click_hunt_demon():
    name = simpledialog.askstring("TG @KAIHUCD", "请输入要猎魔的名字：")
    if name:
        open_website_with_name(name)
 
hunt_demon_button = tk.Button(root, text="全国猎魔", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=1, y=1)  

def open_website_with_data(data):
    url = f"http://doit.cpolar.top/API888?param={data}"
    webbrowser.open_new_tab(url)
 
def on_click_hunt_demon():
    data = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的手机号或身份证：")
    if data:
        open_website_with_data(data)
 
hunt_demon_button = tk.Button(root, text="全国数据", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=190, y=1)  

def open_website_with_legalperson(legalperson):
    url = f"https://www.gsxt.gov.cn/corp-query-homepage.html"
    webbrowser.open_new_tab(url)
 
def on_click_hunt_demon():
    legalperson = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的信用代码：")
    if legalperson:
        open_website_with_legalperson(legalperson)
 
hunt_demon_button = tk.Button(root, text="全国法人", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=380, y=1)  

def open_website_with_name1(name1):
    url = f"https://credit.jiangsu.gov.cn/credit/credit/personal/verificationSearch.do?keyword={name1}"
    webbrowser.open_new_tab(url)
 
def on_click_hunt_demon():
    name1 = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的名字：")
    if name1:
        open_website_with_name1(name1)
 
hunt_demon_button = tk.Button(root, text="全国信用", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=570, y=1)  

def open_website_with_expressdelivery(expressdelivery):
    url = f"http://api.yujn.cn/api/kuaidi.php?type=json&id={expressdelivery}"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    expressdelivery = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的快递单号：")
    if expressdelivery:
        open_website_with_expressdelivery(expressdelivery)

hunt_demon_button = tk.Button(root, text="全国快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=65)  

def open_website_with_company(company):
    url = f"https://www.aiqicha.com/m/?p_type=2&p_tk=7936QasW3VdxFWHjCUyS33A6P8nvOWn7kK%2FnOprANVZEqiXzZIRGMCAVLGHpy60g7LcLsAfJDqIZN4FW9Et5mbogJzrtaC1Bvs9EwSPpXdsdT3Fyj%2Fi%2F4FaIzo39C3nkT9Iuq47DlEaOAGiDpNGgLXukcLso%2B9pKYEtXcJ4p7KHvrwo%3D&p_timestamp=1718654992&p_sign=b8973c041caaf37a42083d8d24917016&p_signature=2900464ac2aa8ba31703f9365e565095&__pc2ps_ab=7936QasW3VdxFWHjCUyS33A6P8nvOWn7kK%2FnOprANVZEqiXzZIRGMCAVLGHpy60g7LcLsAfJDqIZN4FW9Et5mbogJzrtaC1Bvs9EwSPpXdsdT3Fyj%2Fi%2F4FaIzo39C3nkT9Iuq47DlEaOAGiDpNGgLXukcLso%2B9pKYEtXcJ4p7KHvrwo%3D%7C1718654992%7C2900464ac2aa8ba31703f9365e565095%7Cb8973c041caaf37a42083d8d24917016&VNK=fbcfa101"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    company = simpledialog.askstring("TG @KAIHUCD", "输入要查询的公司名称：")
    if company:
        open_website_with_company(company)

hunt_demon_button = tk.Button(root, text="全国公司", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=190, y=65)  

def open_website_with_deadbeat(deadbeat):
    url = f"http://www.13315.top/Page/DishonestyRecord.ashx?_refluxos=a10"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    deadbeat = simpledialog.askstring("TG @KAIHUCD", "请输入查询的姓名：")
    if deadbeat:
        open_website_with_deadbeat(deadbeat)

hunt_demon_button = tk.Button(root, text="全国老赖", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=380, y=65)  

def open_website_with_Subsistenceallowance(Subsistenceallowance):
    url = f"http://php.saxmz.gov.cn/jz_ask_search/index.php?_refluxos=a10"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Subsistenceallowance = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的二要素信息：")
    if Subsistenceallowance:
        open_website_with_Subsistenceallowance(Subsistenceallowance)

hunt_demon_button = tk.Button(root, text="全国低保", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=570, y=65)  

def open_website_with_CommonNumber(CommonNumber):
    url = f"https://login.gjzwfw.gov.cn/tacs-uc/naturalMan/naturalFwd"
    webbrowser.open_new_tab(url)

def open_website_with_Connectcode(Connectcode):
    url = f"http://h5.yezi66.net:90/invite/1299233"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Connectcode = simpledialog.askstring("TG @KAIHUCD", "输入任意数字或文字即可跳转接码平台：")
    if Connectcode:
        open_website_with_Connectcode(Connectcode)

hunt_demon_button = tk.Button(root, text="接码平台", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=1, y=130)  

def open_website_with_bomb(bomb):
    url = f"https://sms.bangtang.top/index.php?hm={bomb}&c=1&_refluxos=a10"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    bomb = simpledialog.askstring("TG @KAIHUCD", "输入要轰炸的手机号：")
    if bomb:
        open_website_with_bomb(bomb)

hunt_demon_button = tk.Button(root, text="短信轰炸", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=190, y=130)  

def open_website_with_Numbersection(Numbersection):
    url = f"https://www.chahaoba.com/"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Numbersection = simpledialog.askstring("TG @KAIHUCD", "输入生成的手机号前三后二以及地区：")
    if Numbersection:
        open_website_with_Numbersection(Numbersection)

hunt_demon_button = tk.Button(root, text="手机号段", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=380, y=130)  

def open_website_with_father(father):
    url = f"https://www.socarchina.com/m/sfz/index.php?_refluxos=a10"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    father = simpledialog.askstring("TG @KAIHUCD", "输入生成的二要素：")
    if father:
        open_website_with_father(father)

hunt_demon_button = tk.Button(root, text="神父生成", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=570, y=130)  

def open_website_with_face(face):
    url = f"https://facecomparison.buyaocha.com/"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    face = simpledialog.askstring("TG @KAIHUCD", "输入任意数字或文字即可跳转人脸对比平台：")
    if face:
        open_website_with_face(face)

hunt_demon_button = tk.Button(root, text="人脸对比", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=1, y=195)  

def open_website_with_space(space):
    url = f"http://www.dall.com.cn/?_refluxos=a10"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    space = simpledialog.askstring("TG @KAIHUCD", "输入任意数字或文字即可跳转空号检测平台：")
    if space:
        open_website_with_space(space)

hunt_demon_button = tk.Button(root, text="空号检测", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=190, y=195)  

def open_website_with_Individualaccounttemplate(Individualaccounttemplate):
    url = f"https://i.hd-r.cn/7557b17f621fe6c991e459614fbb0aa4.jpg"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Individualaccounttemplate = simpledialog.askstring("TG @KAIHUCD", "输入任意数字或文字即可跳转个户模板：")
    if Individualaccounttemplate:
        open_website_with_Individualaccounttemplate(Individualaccounttemplate)

hunt_demon_button = tk.Button(root, text="个户模板", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=380, y=195)  

def open_website_with_FatherTemplate(FatherTemplate):
    url = f"https://i.hd-r.cn/655f86eba86b5d398f35e19c65dd177e.jpg"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    FatherTemplate = simpledialog.askstring("TG @KAIHUCD", "输入任意数字或文字即可跳转神父模板：")
    if FatherTemplate:
        open_website_with_FatherTemplate(FatherTemplate)

hunt_demon_button = tk.Button(root, text="神父模板", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=570, y=195)  

def open_website_with_Homeexpressdelivery(Homeexpressdelivery):
    url = f"http://www.zjs.com.cn/"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Homeexpressdelivery = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的宅急快递单号：")
    if Homeexpressdelivery:
        open_website_with_Homeexpressdelivery(Homeexpressdelivery)

hunt_demon_button = tk.Button(root, text="宅急快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=260)  

def open_website_with_SFexpress(SFexpress):
    url = f"https://www.sf-express.com/chn/sc"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    SFexpress = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的顺丰快递单号：")
    if SFexpress:
        open_website_with_SFexpress(SFexpress)

hunt_demon_button = tk.Button(root, text="顺丰快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=190, y=260)  

def open_website_with_YousuExpress(YousuExpress):
    url = f"https://www.uce.cn/loginregistration/registration"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    YousuExpress = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的优速快递单号：")
    if YousuExpress:
        open_website_with_YousuExpress(YousuExpress)

hunt_demon_button = tk.Button(root, text="优速快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=380, y=260)  

def open_website_with_BestExpress(BestExpress):
    url = f"https://www.800best.com/"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    BestExpress = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的百世快递单号：")
    if BestExpress:
        open_website_with_BestExpress(BestExpress)

hunt_demon_button = tk.Button(root, text="百世快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=570, y=260)  

def open_website_with_ZTO(ZTO):
    url = f"https://m.zto.com/home"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    ZTO = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的中通快递单号：")
    if ZTO:
        open_website_with_ZTO(ZTO)

hunt_demon_button = tk.Button(root, text="中通快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=1, y=325)  

def open_website_with_YundaExpress(YundaExpress):
    url = f"https://web.yundaex.com/h5/#/home"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    YundaExpress = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的韵达快递单号：")
    if YundaExpress:
        open_website_with_YundaExpress(YundaExpress)

hunt_demon_button = tk.Button(root, text="韵达快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=190, y=325)  

def open_website_with_sto(sto):
    url = f"https://www.sto.cn/h5"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    sto = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的申通快递单号：")
    if sto:
        open_website_with_sto(sto)

hunt_demon_button = tk.Button(root, text="申通快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=380, y=325)  

def open_website_with_ems(ems):
    url = f"https://www.ems.com.cn/?FIcMeesb7rhP=1714673420920"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    ems = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的邮政快递单号：")
    if ems:
        open_website_with_ems(ems)

hunt_demon_button = tk.Button(root, text="邮政快递", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=570, y=325)  

def on_click_hunt_demon():
    CommonNumber = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的名字和身份证：")
    if CommonNumber:
        open_website_with_CommonNumber(CommonNumber)

hunt_demon_button = tk.Button(root, text="国政常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=390)  

def open_website_with_TeachersHead(TeachersHead):
    url = f"https://zwfw.moe.gov.cn/ntce/cert/?addrid=a87d9521316442258d3275fe1e790bee&type=hot"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    TeachersHead = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的老师名字和身份证：")
    if TeachersHead:
        open_website_with_TeachersHead(TeachersHead)

hunt_demon_button = tk.Button(root, text="全国教师头", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=390)  

def open_website_with_ProbabilityHead(ProbabilityHead):
    url = f"https://cx.mem.gov.cn/wxcx/pages/certificateQuery/inquirySpecialCertificate?personTypeCode=03"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    ProbabilityHead = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的名字和身份证：")
    if ProbabilityHead:
        open_website_with_ProbabilityHead(ProbabilityHead)

hunt_demon_button = tk.Button(root, text="全国概率头", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=390)  

def open_website_with_Twoelements(Twoelements):
    url = f"https://passport.vivo.com.cn/#/retrieveAccountInput?fromAppeal=1&isHelping=1"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Twoelements = simpledialog.askstring("TG @KAIHUCD", "请输入要验证的名字和身份证：")
    if Twoelements:
        open_website_with_Twoelements(Twoelements)

hunt_demon_button = tk.Button(root, text="二要素验证", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=455)  

def open_website_with_threeelements(threeelements):
    url = f"https://online.bjca.org.cn/#/index?channelId=NVVUTXhBVE0="
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    threeelements = simpledialog.askstring("TG @KAIHUCD", "请输入要验证的名字和身份证和手机号：")
    if threeelements:
        open_website_with_threeelements(threeelements)

hunt_demon_button = tk.Button(root, text="三要素验证", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=455)  

def open_website_with_Fourelements(Fourelements):
    url = f""
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Fourelements = simpledialog.askstring("TG @KAIHUCD", "正在更新中：")
    if Fourelements:
        open_website_with_Fourelements(Fourelements)

hunt_demon_button = tk.Button(root, text="四要素验证", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=455)  

def open_website_with_Guangdong(Guangdong):
    url = f"https://tyrz.gd.gov.cn/pscp/sso/static/m/findaccount/1"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Guangdong = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的广东姓名和身份证（前三后三）：")
    if Guangdong:
        open_website_with_Guangdong(Guangdong)

hunt_demon_button = tk.Button(root, text="广东常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=520)  

def open_website_with_Guangxi(Guangxi):
    url = f"https://tyrz.zwfw.gxzf.gov.cn/portal/gxWeb/html/forgetPswd.html?userType=1"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Guangxi = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的广西姓名和身份证（前三后四）：")
    if Guangxi:
        open_website_with_Guangxi(Guangxi)

hunt_demon_button = tk.Button(root, text="广西常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=520)  

def open_website_with_Hebei(Hebei):
    url = f"https://zwfw.hebei.gov.cn/hbjis/front/findpwd/step1.do?userType=1&findWay=1"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Hebei = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的河北姓名和身份证（前三后四）：")
    if Hebei:
        open_website_with_Hebei(Hebei)

hunt_demon_button = tk.Button(root, text="河北常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=520)  

def open_website_with_Henan(Henan):
    url = f"https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/naturalFwd"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Henan = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的河南姓名和身份证（前三后四）：")
    if Henan:
        open_website_with_Henan(Henan)

hunt_demon_button = tk.Button(root, text="河南常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=585)  

def open_website_with_Hubei(Hubei):
    url = f"https://oauth.hubei.gov.cn:8443/hbyzw/zwfw/userInfo/findPwd.jsp?appCode=hbzwfw&zwfwtype=psn"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Hubei = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的湖北姓名和身份证（前三后四）：")
    if Hubei:
        open_website_with_Hubei(Hubei)

hunt_demon_button = tk.Button(root, text="湖北常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=585)  

def open_website_with_Hunan(Hunan):
    url = f"https://auth.zwfw.hunan.gov.cn/oauth2/register/forgetpwd"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Hunan = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的湖南姓名和身份证（前三后四）：")
    if Hunan:
        open_website_with_Hunan(Hunan)

hunt_demon_button = tk.Button(root, text="湖南常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=585)  

def open_website_with_Shandong(Shandong):
    url = f"https://tysfrz.isdapp.shandong.gov.cn/jis-web/login_m?appMark=OWWNSJVCC&userType=1&gbTrust=false&backUrl=http%3A%2F%2Fwww.shandong.gov.cn%2Fapi-gateway%2Fjpaas-juspace-web-sdywtb%2Ffront%2Fsso%2Flogin-success%3Fgotourl%3DaHR0cDovL3d3dy5zaGFuZG9uZy5nb3YuY24vYXBpLWdhdGV3YXkvanBhYXMtamlxLXdlYi1zZHl3dGIvZnJvbnQvaXRlbS9ncl9pbmRleA%3D%3D"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Shandong = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的山东姓名和身份证（前三后二）：")
    if Shandong:
        open_website_with_Shandong(Shandong)

hunt_demon_button = tk.Button(root, text="山东常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=650)  

def open_website_with_Shanxi(Shanxi):
    url = f"https://www.sxzwfw.gov.cn/v5/auth/#/forget-pwd?utype=0"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Shanxi = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的山西姓名和身份证（前空后四）：")
    if Shanxi:
        open_website_with_Shanxi(Shanxi)

hunt_demon_button = tk.Button(root, text="山西常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=650)  

def open_website_with_Liaoning(Liaoning):
    url = f"https://center.lnzwfw.gov.cn/api/retrievePassword/toSelectUserType"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Liaoning = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的辽宁姓名和身份证（前三后四）：")
    if Liaoning:
        open_website_with_Liaoning(Liaoning)

hunt_demon_button = tk.Button(root, text="辽宁常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=650)  

def open_website_with_Jilin(Jilin):
    url = f"https://user.jl.gov.cn/forget/natural?redirect=http%3A%2F%2Fzwfw.jl.gov.cn%2Fjlszwfw%2F"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Jilin = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的吉林姓名和身份证（前三后四）：")
    if Jilin:
        open_website_with_Jilin(Jilin)

hunt_demon_button = tk.Button(root, text="吉林常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=715)  

def open_website_with_Jiangsu(Jiangsu):
    url = f"https://www.jszwfw.gov.cn/jsjis/front/findpwd/step1.do"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Jiangsu = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的江苏姓名和身份证（前三后四）：")
    if Jiangsu:
        open_website_with_Jiangsu(Jiangsu)

hunt_demon_button = tk.Button(root, text="江苏常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=715)  

def open_website_with_Anhui(Anhui):
    url = f"https://sso.ahzwfw.gov.cn/uccp-user/resources/forgetPsd/forgetPsd-phone?callback="
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Anhui = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的安徽姓名和身份证（前三后四）：")
    if Anhui:
        open_website_with_Anhui(Anhui)

hunt_demon_button = tk.Button(root, text="安徽常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=715)  

def open_website_with_Sichuan(Sichuan):
    url = f"https://rzsc.sczwfw.gov.cn/portal/newPerson/pc/forgetPassword_Step1_V2.jsp?_refluxos=a10"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Sichuan = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的四川姓名和身份证（前三后二）：")
    if Sichuan:
        open_website_with_Sichuan(Sichuan)

hunt_demon_button = tk.Button(root, text="四川常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=780)  

def open_website_with_Jiangxi(Jiangxi):
    url = f"https://gftjis.jxzwfww.gov.cn/jisgft/front/findpwd/step1.do"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Jiangxi = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的江西姓名和身份证（前三后四）：")
    if Jiangxi:
        open_website_with_Jiangxi(Jiangxi)

hunt_demon_button = tk.Button(root, text="江西常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=780)  

def open_website_with_Hainan(Hainan):
    url = f"https://ucs-sso.digitalhainan.com.cn/outer?entry_type=gov&page_type=login&lang=zh&flag=false"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Hainan = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的海南姓名和身份证（前三后四）：")
    if Hainan:
        open_website_with_Hainan(Hainan)

hunt_demon_button = tk.Button(root, text="海南常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=780)  

def open_website_with_Guizhou(Guizhou):
    url = f"https://smrz.zwfw.guizhou.gov.cn/sso/login?utype=0&redirect=istrue&client_id=5ZYPTXH7G&goto=http://zwfw.guizhou.gov.cn/api/oauth/return_url.aspx?oauth_guid=d65d6b3c-4ca5-4f4c-8d3f-8d6b41e3cc1a"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Guizhou = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的贵州姓名和身份证（前三后四）：")
    if Guizhou:
        open_website_with_Guizhou(Guizhou)

hunt_demon_button = tk.Button(root, text="贵州常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=845)  

def open_website_with_Qinghai(Qinghai):
    url = f"https://uams.qhzwfw.gov.cn/portal/gxWeb/html/forget1.html"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Qinghai = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的青海姓名和身份证（前三后四）：")
    if Qinghai:
        open_website_with_Qinghai(Qinghai)

hunt_demon_button = tk.Button(root, text="青海常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=845)  

def open_website_with_Shanghai(Shanghai):
    url = f"https://zwdtuser.sh.gov.cn/uc/forget/RetrievePassword.html"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Shanghai = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的上海姓名和身份证（前三后四）：")
    if Shanghai:
        open_website_with_Shanghai(Shanghai)

hunt_demon_button = tk.Button(root, text="上海常用号", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=845)  

def open_website_with_HubeiFuzzyMachineOwner(HubeiFuzzyMachineOwner):
    url = f"https://tysfrz.isdapp.shandong.gov.cn/jis-web/login?appMark=OWWNSJVCC&userType=1&gbTrust=false&backUrl=http%3A%2F%2Fwww.shandong.gov.cn%2Fapi-gateway%2Fjpaas-juspace-web-sdywtb%2Ffront%2Fsso%2Flogin-success%3Fgotourl%3DaHR0cDovL3d3dy5zaGFuZG9uZy5nb3YuY24vYXBpLWdhdGV3YXkvanBhYXMtanVzcGFjZS13ZWItc2R5d3RiL2Zyb250L2xvZ2luL3VybEFkZFRpY2tldD91cmw9aHR0cDovL3d3dy5zaGFuZG9uZy5nb3YuY24vL2FwaS1nYXRld2F5L2pwYWFzLWp1c3BhY2Utd2ViLXNkeXd0Yi9mcm9udC9zYnRjL3NiX2luZGV4"
    webbrowser.open_new_tab(url)
 
def on_click_hunt_demon():
    HubeiFuzzyMachineOwner = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的山东手机号（前一后一）\n需要抓包 抓此包看响应text\nhttps://tysfrz.isdapp.shandong.gov.cn/jpaas-jis-p\neruser-server/front/findpwd/step-one：")
    if HubeiFuzzyMachineOwner:
        open_website_with_HubeiFuzzyMachineOwner(HubeiFuzzyMachineOwner)
 
hunt_demon_button = tk.Button(root, text="山东模糊机", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=0, y=910)  

def open_website_with_HebeiFuzzyMachineOwner(HebeiFuzzyMachineOwner):
    url = f"https://zwfw.hebei.gov.cn/hbjis/front/findpwd/step1.do?userType=1&findWay=1"
    webbrowser.open_new_tab(url)
 
def on_click_hunt_demon():
    HebeiFuzzyMachineOwner = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的河北手机号（后四）\n需要抓包 抓此包看响应text\nhttps://zwfw.hebei.gov.cn/hbjis/front/findpwd/st\nep2.do?type=2：")
    if HebeiFuzzyMachineOwner:
        open_website_with_HebeiFuzzyMachineOwner(HebeiFuzzyMachineOwner)
 
hunt_demon_button = tk.Button(root, text="河北模糊机", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=220, y=910)  

def open_website_with_Jiangxifuzzymachine(Jiangxifuzzymachine):
    url = f"https://gftjis.jxzwfww.gov.cn/jisgft/front/findpwd/step1.do"
    webbrowser.open_new_tab(url)
 
def on_click_hunt_demon():
    Jiangxifuzzymachine = simpledialog.askstring("TG @KAIHUCD", "请输入要查询的江西手机号（后四）\n需要抓包 抓此包看响应text\nhttps://gftjis.jxzwfww.gov.cn/jisgft/front/manual\nauth/step1_show.do：")
    if Jiangxifuzzymachine:
        open_website_with_Jiangxifuzzymachine(Jiangxifuzzymachine)
 
hunt_demon_button = tk.Button(root, text="江西模糊机", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=440, y=910)  

def copy_text_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    clipboard = simpledialog.askstring("TG @KAIHUCD", "已复制频道链接或作者TG号")

btn_copy_group = tk.Button(root, text="加入频道", fg="red", font=("Arial", 8), command=lambda: copy_text_to_clipboard("https://t.me/SGSNBYYDS"))
btn_copy_group.place(x=0, y=1405)  

btn_copy_number = tk.Button(root, text="联系作者", fg="red", font=("Arial", 8), command=lambda: copy_text_to_clipboard("@KAIHUCD"))
btn_copy_number.place(x=190, y=1405)  

def open_website_with_sponsor(sponsor):
    url = f"https://i.hd-r.cn/ffccc8a8cba223cce52cb61b17fc40bc.png"
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    sponsor = simpledialog.askstring("TG @KAIHUCD", "输入任意数字或文字即可跳转收款码")
    if sponsor:
        open_website_with_sponsor(sponsor)

hunt_demon_button = tk.Button(root, text="赞助作者", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=380, y=1405)  

def open_website_with_Notice(Notice):
    url = f""
    webbrowser.open_new_tab(url)

def on_click_hunt_demon():
    Notice = simpledialog.askstring("TG @KAIHUCD", "=================关于作者=================\n脚本作者：BY.伤感神\n伤感神频道：https://t.me/SGSNBYYDS\n伤感神TG号：@KAIHUCD\n=================关于公告=================\n目前版本：1.6\n目前脚本：公益\n禁止任何倒卖\n禁止任何二改\n=================脚本内容=================\n更新宅急快递\n更新顺丰快递\n更新优速快递\n更新百世快递\n更新中通快递\n更新韵达快递\n更新申通快递\n更新邮政快递")
    if Notice:
        open_website_with_Notice(Notice)

hunt_demon_button = tk.Button(root, text="脚本公告", command=on_click_hunt_demon, fg='red', font=("Arial", 8))
hunt_demon_button.place(x=570, y=1405)  

# 运行主循环
root.mainloop()
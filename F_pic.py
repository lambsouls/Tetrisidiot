#!/usr/bin/env python
# coding: utf-8

# In[15]:


def picTo2():
    """图片灰化+二值化"""
    # 图片二值化
    from PIL import Image
    img = Image.open('png.bmp')
 
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = img.convert('L')
    Img.save("png1.bmp")
 
    #Img = img.resize((80,60))
    #Img.save("png1.bmp")
    
    
    # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
    threshold = 50
 
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
 
    # 图片二值化
    photo = Img.point(table, '1')
    photo.save("png2.bmp")


# In[2]:


def picpixel(x,y):
    """xy坐标的颜色二值"""
    from PIL import Image

    img1=Image.open("png2.bmp")

    return(str(int(bool(img1.getpixel((x,y))))))


# In[14]:


def pic200():
    """200个关键的的二值"""
    
    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=[128,147,166,185,204,223,240,258,276,292]
    y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20=[109,126,150,167,179,201,219,238,255,276,293,312,329,348,365,381,400,420,434,455]    

    a10=picpixel(x0,y1)
    a11=picpixel(x1,y1)
    a12=picpixel(x2,y1)
    a13=picpixel(x3,y1)
    a14=picpixel(x4,y1)
    a15=picpixel(x5,y1)
    a16=picpixel(x6,y1)
    a17=picpixel(x7,y1)
    a18=picpixel(x8,y1)
    a19=picpixel(x9,y1)
    
    a20=picpixel(x0,y2)
    a21=picpixel(x1,y2)
    a22=picpixel(x2,y2)
    a23=picpixel(x3,y2)
    a24=picpixel(x4,y2)
    a25=picpixel(x5,y2)
    a26=picpixel(x6,y2)
    a27=picpixel(x7,y2)
    a28=picpixel(x8,y2)
    a29=picpixel(x9,y2)
    
    a30=picpixel(x0,y3)
    a31=picpixel(x1,y3)
    a32=picpixel(x2,y3)
    a33=picpixel(x3,y3)
    a34=picpixel(x4,y3)
    a35=picpixel(x5,y3)
    a36=picpixel(x6,y3)
    a37=picpixel(x7,y3)
    a38=picpixel(x8,y3)
    a39=picpixel(x9,y3)
    
    a40=picpixel(x0,y4)
    a41=picpixel(x1,y4)
    a42=picpixel(x2,y4)
    a43=picpixel(x3,y4)
    a44=picpixel(x4,y4)
    a45=picpixel(x5,y4)
    a46=picpixel(x6,y4)
    a47=picpixel(x7,y4)
    a48=picpixel(x8,y4)
    a49=picpixel(x9,y4)
    
    a50=picpixel(x0,y5)
    a51=picpixel(x1,y5)
    a52=picpixel(x2,y5)
    a53=picpixel(x3,y5)
    a54=picpixel(x4,y5)
    a55=picpixel(x5,y5)
    a56=picpixel(x6,y5)
    a57=picpixel(x7,y5)
    a58=picpixel(x8,y5)
    a59=picpixel(x9,y5)

    a60=picpixel(x0,y6)
    a61=picpixel(x1,y6)
    a62=picpixel(x2,y6)
    a63=picpixel(x3,y6)
    a64=picpixel(x4,y6)
    a65=picpixel(x5,y6)
    a66=picpixel(x6,y6)
    a67=picpixel(x7,y6)
    a68=picpixel(x8,y6)
    a69=picpixel(x9,y6)
    
    a70=picpixel(x0,y7)
    a71=picpixel(x1,y7)
    a72=picpixel(x2,y7)
    a73=picpixel(x3,y7)
    a74=picpixel(x4,y7)
    a75=picpixel(x5,y7)
    a76=picpixel(x6,y7)
    a77=picpixel(x7,y7)
    a78=picpixel(x8,y7)
    a79=picpixel(x9,y7)
    
    a80=picpixel(x0,y8)
    a81=picpixel(x1,y8)
    a82=picpixel(x2,y8)
    a83=picpixel(x3,y8)
    a84=picpixel(x4,y8)
    a85=picpixel(x5,y8)
    a86=picpixel(x6,y8)
    a87=picpixel(x7,y8)
    a88=picpixel(x8,y8)
    a89=picpixel(x9,y8)
    
    a90=picpixel(x0,y9)
    a91=picpixel(x1,y9)
    a92=picpixel(x2,y9)
    a93=picpixel(x3,y9)
    a94=picpixel(x4,y9)
    a95=picpixel(x5,y9)
    a96=picpixel(x6,y9)
    a97=picpixel(x7,y9)
    a98=picpixel(x8,y9)
    a99=picpixel(x9,y9)
    
    a100=picpixel(x0,y10)
    a101=picpixel(x1,y10)
    a102=picpixel(x2,y10)
    a103=picpixel(x3,y10)
    a104=picpixel(x4,y10)
    a105=picpixel(x5,y10)
    a106=picpixel(x6,y10)
    a107=picpixel(x7,y10)
    a108=picpixel(x8,y10)
    a109=picpixel(x9,y10)
    
    a110=picpixel(x0,y11)
    a111=picpixel(x1,y11)
    a112=picpixel(x2,y11)
    a113=picpixel(x3,y11)
    a114=picpixel(x4,y11)
    a115=picpixel(x5,y11)
    a116=picpixel(x6,y11)
    a117=picpixel(x7,y11)
    a118=picpixel(x8,y11)
    a119=picpixel(x9,y11)
    
    a120=picpixel(x0,y12)
    a121=picpixel(x1,y12)
    a122=picpixel(x2,y12)
    a123=picpixel(x3,y12)
    a124=picpixel(x4,y12)
    a125=picpixel(x5,y12)
    a126=picpixel(x6,y12)
    a127=picpixel(x7,y12)
    a128=picpixel(x8,y12)
    a129=picpixel(x9,y12)
    
    a130=picpixel(x0,y13)
    a131=picpixel(x1,y13)
    a132=picpixel(x2,y13)
    a133=picpixel(x3,y13)
    a134=picpixel(x4,y13)
    a135=picpixel(x5,y13)
    a136=picpixel(x6,y13)
    a137=picpixel(x7,y13)
    a138=picpixel(x8,y13)
    a139=picpixel(x9,y13)
    
    a140=picpixel(x0,y14)
    a141=picpixel(x1,y14)
    a142=picpixel(x2,y14)
    a143=picpixel(x3,y14)
    a144=picpixel(x4,y14)
    a145=picpixel(x5,y14)
    a146=picpixel(x6,y14)
    a147=picpixel(x7,y14)
    a148=picpixel(x8,y14)
    a149=picpixel(x9,y14)
    
    a150=picpixel(x0,y15)
    a151=picpixel(x1,y15)
    a152=picpixel(x2,y15)
    a153=picpixel(x3,y15)
    a154=picpixel(x4,y15)
    a155=picpixel(x5,y15)
    a156=picpixel(x6,y15)
    a157=picpixel(x7,y15)
    a158=picpixel(x8,y15)
    a159=picpixel(x9,y15)
    
    a160=picpixel(x0,y16)
    a161=picpixel(x1,y16)
    a162=picpixel(x2,y16)
    a163=picpixel(x3,y16)
    a164=picpixel(x4,y16)
    a165=picpixel(x5,y16)
    a166=picpixel(x6,y16)
    a167=picpixel(x7,y16)
    a168=picpixel(x8,y16)
    a169=picpixel(x9,y16)
    
    a170=picpixel(x0,y17)
    a171=picpixel(x1,y17)
    a172=picpixel(x2,y17)
    a173=picpixel(x3,y17)
    a174=picpixel(x4,y17)
    a175=picpixel(x5,y17)
    a176=picpixel(x6,y17)
    a177=picpixel(x7,y17)
    a178=picpixel(x8,y17)
    a179=picpixel(x9,y17)
    
    a180=picpixel(x0,y18)
    a181=picpixel(x1,y18)
    a182=picpixel(x2,y18)
    a183=picpixel(x3,y18)
    a184=picpixel(x4,y18)
    a185=picpixel(x5,y18)
    a186=picpixel(x6,y18)
    a187=picpixel(x7,y18)
    a188=picpixel(x8,y18)
    a189=picpixel(x9,y18)
    
    a190=picpixel(x0,y19)
    a191=picpixel(x1,y19)
    a192=picpixel(x2,y19)
    a193=picpixel(x3,y19)
    a194=picpixel(x4,y19)
    a195=picpixel(x5,y19)
    a196=picpixel(x6,y19)
    a197=picpixel(x7,y19)
    a198=picpixel(x8,y19)
    a199=picpixel(x9,y19)
    
    a200=picpixel(x0,y20)
    a201=picpixel(x1,y20)
    a202=picpixel(x2,y20)
    a203=picpixel(x3,y20)
    a204=picpixel(x4,y20)
    a205=picpixel(x5,y20)
    a206=picpixel(x6,y20)
    a207=picpixel(x7,y20)
    a208=picpixel(x8,y20)
    a209=picpixel(x9,y20)
    
    a="1"
    
    return(int((a+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31+a32+a33+a34+a35+a36+a37+a38+a39+a40+a41+a42+a43+a44+a45+a46+a47+a48+a49+a50+a51+a52+a53+a54+a55+a56+a57+a58+a59+a60+a61+a62+a63+a64+a65+a66+a67+a68+a69+a70+a71+a72+a73+a74+a75+a76+a77+a78+a79+a80+a81+a82+a83+a84+a85+a86+a87+a88+a89+a90+a91+a92+a93+a94+a95+a96+a97+a98+a99+a100+a101+a102+a103+a104+a105+a106+a107+a108+a109+a110+a111+a112+a113+a114+a115+a116+a117+a118+a119+a120+a121+a122+a123+a124+a125+a126+a127+a128+a129+a130+a131+a132+a133+a134+a135+a136+a137+a138+a139+a140+a141+a142+a143+a144+a145+a146+a147+a148+a149+a150+a151+a152+a153+a154+a155+a156+a157+a158+a159+a160+a161+a162+a163+a164+a165+a166+a167+a168+a169+a170+a171+a172+a173+a174+a175+a176+a177+a178+a179+a180+a181+a182+a183+a184+a185+a186+a187+a188+a189+a190+a191+a192+a193+a194+a195+a196+a197+a198+a199+a200+a201+a202+a203+a204+a205+a206+a207+a208+a209)))


# In[16]:


def pic_11():
    """自动开始游戏"""
    import pyautogui
    p=picpixel(343,146)
    if p==255:
        print("点击开始游戏")
        #298，504
        pyautogui.moveTo(298,504,)
        pyautogui.click()
        


# In[ ]:





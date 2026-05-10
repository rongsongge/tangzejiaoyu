import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ====================== 终极隐藏版：本地运行也能彻底隐藏Deploy按钮 ======================
st.markdown("""
<style>
/* 1. 隐藏右上角三点菜单 */
#MainMenu {visibility: hidden !important;}

/* 2. 隐藏右上角Deploy按钮（本地模式） */
div[data-testid="stDeployButton"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* 3. 隐藏顶部红色装饰条 */
[data-testid="stDecoration"] {display: none !important;}

/* 4. 隐藏底部版权信息 */
footer {visibility: hidden !important;}

/* 5. 保留侧边栏开关按钮 */
button[kind="secondary"][data-testid="baseButton-secondary"] {
    visibility: visible !important;
    display: block !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------------
# 页面基础设置
# ----------------------
st.set_page_config(
    page_title="塘泽教育",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 管理员密码
ADMIN_PASSWORD = "045571"

# 初始化状态
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False
if "edit_idx" not in st.session_state:
    st.session_state.edit_idx = None

# ----------------------
# 访问人数统计
# ----------------------
if "visit_count" not in st.session_state:
    if not os.path.exists("visit_count.txt"):
        with open("visit_count.txt", "w") as f:
            f.write("0")
    with open("visit_count.txt", "r") as f:
        count = int(f.read())
    count += 1
    with open("visit_count.txt", "w") as f:
        f.write(str(count))
    st.session_state.visit_count = count
else:
    count = st.session_state.visit_count

# ----------------------
# 读取报名数据通用函数（电话列强制为字符串，修复报错）
# ----------------------
def load_sign_data():
    if os.path.exists("报名记录.csv"):
        return pd.read_csv("报名记录.csv", encoding="utf-8-sig", dtype={"电话": str})
    else:
        return pd.DataFrame(columns=["提交时间","姓名","电话","意向课程","电脑基础","备注"])

def save_sign_data(df):
    df["电话"] = df["电话"].astype(str)
    df.to_csv("报名记录.csv", index=False, encoding="utf-8-sig")

# ----------------------
# 顶部LOGO
# ----------------------
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("logo.png", width=150)
with col_title:
    st.title("💻 塘泽教育 — 专业电脑基础技能培训")

st.markdown("---")

# ----------------------
# 侧边栏导航
# ----------------------
st.sidebar.title("🏠 导航菜单")
menu = st.sidebar.radio(
    "请选择查看项目：",
    ("🏠 学校首页",
     "📝 办公应用",
     "🎨 平面设计",
     "🎬 视频制作",
     "📦 产品建模",
     "🏠 室内设计",
     "⚙️ 机电绘图",
     "🌐 网页制作",
     "💰 课程价格",
     "👨‍🏫 老师介绍",
     "📝 在线报名",
     "🔐 管理员后台")
)

# ----------------------
# 1. 学校首页
# ----------------------
if menu == "🏠 学校首页":
    st.title("💻 塘泽教育 — 欢迎您！")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("🎯 学校简介")
        st.write("""
        塘泽教育专注电脑基础技能培训多年，课程实用、易学、好就业。
        从零基础到精通，全程实战教学，学会为止！
        我们承诺：小班教学、随到随学、免费重学、推荐就业。
        """)
        st.subheader("🌟 我们的优势")
        st.write("""
        ✅ 零基础可学  
        ✅ 小班教学 / 一对一辅导  
        ✅ 实战案例教学  
        ✅ 免费重学 / 推荐就业  
        """)
    with col2:
        st.info("💡 提示：左侧菜单可查看课程详情、价格和老师介绍")

    st.subheader("📚 开设课程总览")
    st.success("""
    📝 **办公应用类**：电脑基础、Word、Excel、PPT、飞书文档  
    🎨 **平面设计类**：PS、AI、CDR、ID  
    🎬 **视频制作类**：剪映、PR、AE  
    📦 **产品建模类**：C4D、Blender  
    🏠 **室内设计类**：CAD、3Dmax、酷家乐  
    ⚙️ **机电绘图类**：CAD、CREO、SW、EPLAN  
    🌐 **网页制作类**：DW、VSCode、Python+Streamlit  
    """)

# ----------------------
# 2. 办公应用
# ----------------------
elif menu == "📝 办公应用":
    st.title("📝 办公应用培训课程")
    st.markdown("---")
    st.subheader("适合人群：文员、行政、财务、助理、职场新人、企业办公人员")
    st.info("零基础学习，轻松掌握办公自动化+企业协同办公")
    st.subheader("📖 课程内容")
    st.write("""
    1️⃣ **电脑基础**：电脑操作、打字、文件管理、上网、常用软件安装  
    2️⃣ **文字排版 Word**：文档排版、表格、图文混排、合同、简历  
    3️⃣ **电子表格 Excel**：表格制作、函数公式、数据透视表、图表、财务报表  
    4️⃣ **演示文稿 PPT**：课件制作、汇报PPT、动画、幻灯片设计  
    5️⃣ **飞书文档**：企业协同办公、在线文档编辑、表格、云空间、团队共享、高效办公协作  
    """)
    st.subheader("🎓 学完可从事")
    st.success("文员、行政、出纳、数据统计、办公室内勤、企业协同办公专员等岗位")

# ----------------------
# 3. 平面设计
# ----------------------
elif menu == "🎨 平面设计":
    st.title("🎨 平面设计培训课程")
    st.markdown("---")
    st.subheader("适合人群：设计师、广告、图文店、美工、创业者")
    st.info("零基础可学，学成可接单、就业")
    st.subheader("📖 课程内容")
    st.write("""
    1️⃣ **图片处理 PS**：修图、调色、海报、logo、摄影后期  
    2️⃣ **矢量绘图 AI**：logo、字体设计、插画、矢量图制作  
    3️⃣ **平面作图 CDR**：宣传单、名片、画册、包装、展板  
    4️⃣ **平面排版 ID**：书籍、画册、杂志、多页排版设计  
    """)
    st.subheader("🎓 学完可从事")
    st.success("广告设计师、图文店、美工、电商设计、自由接单、排版设计师")

# ----------------------
# 4. 视频制作
# ----------------------
elif menu == "🎬 视频制作":
    st.title("🎬 视频制作培训课程")
    st.markdown("---")
    st.subheader("适合人群：短视频创作者、剪辑师、新媒体运营、影视爱好者")
    st.info("零基础入门，掌握短视频、宣传片、特效制作全流程")
    st.subheader("📖 课程内容")
    st.write("""
    1️⃣ **剪映**：零基础短视频剪辑、字幕自动生成、特效、转场、模板使用、抖音/快手短视频制作  
    2️⃣ **视频剪辑 PR**：专业剪辑、调色、音频处理、宣传片剪辑、商业视频制作  
    3️⃣ **特效合成 AE**：动态特效、MG动画、合成、片头片尾、广告高级特效  
    """)
    st.subheader("🎓 学完可从事")
    st.success("短视频剪辑师、影视后期、新媒体运营、广告制作、自由接单、自媒体创作者")

# ----------------------
# 5. 产品建模
# ----------------------
elif menu == "📦 产品建模":
    st.title("📦 产品建模培训课程")
    st.markdown("---")
    st.subheader("适合人群：电商美工、产品设计师、3D建模爱好者、动画行业")
    st.info("掌握产品建模、渲染、动画制作，打造电商爆款主图")
    st.subheader("📖 课程内容")
    st.write("""
    1️⃣ **C4D产品建模**：产品建模、材质、灯光、渲染、电商场景、动态海报  
    2️⃣ **Blender建模渲染**：3D建模、雕刻、渲染、动画、产品可视化  
    """)
    st.subheader("🎓 学完可从事")
    st.success("电商3D美工、产品渲染师、三维建模师、动画制作、游戏建模")

# ----------------------
# 6. 室内设计
# ----------------------
elif menu == "🏠 室内设计":
    st.title("🏠 室内设计培训课程")
    st.markdown("---")
    st.subheader("适合人群：室内设计师、装修行业、全屋定制")
    st.info("从量房到效果图，全流程教学")
    st.subheader("📖 课程内容")
    st.write("""
    1️⃣ **施工图 CAD**：平面、立面、节点图、施工图纸绘制  
    2️⃣ **效果图 3Dmax**：建模、材质、灯光、渲染、全景图  
    3️⃣ **酷家乐**：快速效果图、全屋定制、720°全景  
    """)
    st.subheader("🎓 学完可从事")
    st.success("室内设计师、全屋定制设计师、装修绘图员、效果图设计师")

# ----------------------
# 7. 机电绘图
# ----------------------
elif menu == "⚙️ 机电绘图":
    st.title("⚙️ 机电绘图培训课程")
    st.markdown("---")
    st.subheader("适合人群：机械、电工、设备、模具、钣金行业")
    st.info("企业实战教学，就业面广")
    st.subheader("📖 课程内容")
    st.write("""
    1️⃣ **机械CAD**：零件图、装配图、机械制图标准  
    2️⃣ **CREO**：三维建模、零件设计、装配、工程图  
    3️⃣ **SolidWorks(SW)**：机械建模、装配、工程图、钣金设计  
    4️⃣ **EPLAN**：电气原理图、PLC图纸、电工设计  
    """)
    st.subheader("🎓 学完可从事")
    st.success("机械设计师、电气绘图员、设备设计、模具设计、钣金设计")

# ----------------------
# 8. 网页制作
# ----------------------
elif menu == "🌐 网页制作":
    st.title("🌐 网页制作培训课程")
    st.markdown("---")
    st.subheader("适合人群：零基础想做网站、小程序、个人网页的学员")
    st.info("从入门基础到实战，学会自己做网站！")
    st.subheader("📖 课程内容")
    st.write("""
    1️⃣ **入门基础 DW**：Dreamweaver 软件使用、HTML基础标签、CSS样式、简单网页制作  
    2️⃣ **代码编辑 VSCode**：VSCode 安装配置、插件使用、HTML/CSS/JS代码编写、网页调试  
    3️⃣ **Python+Streamlit网页制作**：Python基础语法、Streamlit 框架使用、表单制作、数据存储、部署上线  
    """)
    st.subheader("🎓 学完可从事")
    st.success("个人网站搭建、企业官网制作、数据可视化网页、接单制作小程序/网站")

# ----------------------
# 9. 课程价格
# ----------------------
elif menu == "💰 课程价格":
    st.title("💰 课程价格表")
    st.markdown("---")

    price_data = {
        "课程类别": ["办公应用", "办公应用", "办公应用", "办公应用", "办公应用",
                     "平面设计", "平面设计", "平面设计", "平面设计",
                     "视频制作", "视频制作", "视频制作",
                     "产品建模", "产品建模",
                     "室内设计", "室内设计", "室内设计",
                     "机电绘图", "机电绘图", "机电绘图", "机电绘图",
                     "网页制作", "网页制作", "网页制作"],
        "课程名称": ["电脑基础", "Word", "Excel", "PPT", "飞书文档",
                     "PS", "AI", "CDR", "ID",
                     "剪映", "PR剪辑", "AE特效",
                     "C4D建模", "Blender建模",
                     "CAD施工图", "3Dmax效果图", "酷家乐",
                     "机械CAD", "CREO", "SolidWorks(SW)", "EPLAN",
                     "DW网页基础", "VSCode代码编辑", "Python+Streamlit网页制作"],
        "课时": ["20课时", "30课时", "40课时", "20课时", "20课时",
                 "60课时", "40课时", "40课时", "30课时",
                 "30课时", "50课时", "60课时",
                 "60课时", "60课时",
                 "60课时", "80课时", "30课时",
                 "60课时", "80课时", "80课时", "60课时",
                 "30课时", "40课时", "60课时"],
        "原价(元)": ["500", "800", "1000", "600", "600",
                     "1800", "1500", "1500", "1200",
                     "800", "1600", "1800",
                     "2200", "2200",
                     "2000", "3000", "1200",
                     "2000", "3000", "3000", "2500",
                     "1000", "1200", "1800"],
        "优惠价(元)": ["399", "699", "899", "499", "499",
                       "1599", "1299", "1299", "999",
                       "599", "1399", "1599",
                       "1999", "1999",
                       "1799", "2699", "999",
                       "1799", "2699", "2699", "2199",
                       "899", "1099", "1599"]
    }
    df_price = pd.DataFrame(price_data)
    st.dataframe(df_price, use_container_width=True)
    st.warning("⚠️ 价格可根据活动调整，咨询老师获取最新优惠！")

# ----------------------
# 10. 老师介绍
# ----------------------
elif menu == "👨‍🏫 老师介绍":
    st.title("👨‍🏫 专业师资团队")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👩‍💼 李老师（办公应用）")
        st.write("✅ 办公软件教学10年经验\n✅ 擅长Word/Excel/PPT/飞书文档高级应用\n✅ 曾为多家企业做办公内训")
        st.info("教学风格：耐心细致，零基础也能听懂")
    with col2:
        st.subheader("🎨 王老师（平面设计）")
        st.write("✅ 平面设计行业8年经验\n✅ 精通PS/AI/CDR/ID全流程\n✅ 学员作品多次获奖")
        st.info("教学风格：实战案例教学，边做边学")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("🎬 陈老师（视频/建模）")
        st.write("✅ 影视后期三维行业7年经验\n✅ 精通剪映/PR/AE/C4D/Blender\n✅ 电商短视频项目实战")
        st.info("教学风格：紧跟行业，实用为主")
    with col4:
        st.subheader("🏠 张老师（室内设计）")
        st.write("✅ 室内设计12年实战经验\n✅ 精通CAD/3Dmax/酷家乐\n✅ 大型家装项目落地经验")
        st.info("教学风格：理论+实战，上手快")

    col5, col6 = st.columns(2)
    with col5:
        st.subheader("⚙️ 刘老师（机电绘图）")
        st.write("✅ 机械机电行业10年经验\n✅ 精通CAD/CREO/SW/EPLAN\n✅ 工厂一线技术出身")
        st.info("教学风格：贴合工厂，实用性强")
    with col6:
        st.subheader("💻 周老师（网页制作）")
        st.write("✅ 网页开发行业6年经验\n✅ 精通DW/VSCode/Python+Streamlit\n✅ 个人网站、企业官网实战教学")
        st.info("教学风格：通俗易懂，手把手教你做网站")

# ----------------------
# 11. 在线报名
# ----------------------
elif menu == "📝 在线报名":
    st.title("📝 塘泽教育 — 在线报名")
    st.markdown("---")

    with st.form("报名表单"):
        name = st.text_input("您的姓名 *")
        phone = st.text_input("联系电话 *")
        course = st.selectbox("意向课程", ["办公应用", "平面设计", "视频制作", "产品建模", "室内设计", "机电绘图", "网页制作", "其他咨询"])
        level = st.radio("电脑基础情况", ["零基础", "有一点基础", "有一定基础"])
        remark = st.text_area("留言/问题（可选）")
        submit = st.form_submit_button("✅ 提交报名信息")

    if submit:
        if not name or not phone:
            st.error("❌ 姓名和电话为必填项，请填写完整！")
        else:
            df = load_sign_data()
            new_data = pd.DataFrame({
                "提交时间": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "姓名": [name],
                "电话": [str(phone)],
                "意向课程": [course],
                "电脑基础": [level],
                "备注": [remark]
            })
            df = pd.concat([df, new_data], ignore_index=True)
            save_sign_data(df)
            st.success("✅ 提交成功！我们会尽快联系您！")
            st.balloons()

# ----------------------
# 12. 管理员后台
# ----------------------
elif menu == "🔐 管理员后台":
    st.title("🔐 管理员后台 — 报名记录管理")
    st.markdown("---")

    if not st.session_state.admin_logged_in:
        st.subheader("请输入管理员密码")
        pwd = st.text_input("密码", type="password")
        if st.button("登录"):
            if pwd == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ 密码错误！")
    else:
        df = load_sign_data()
        if df.empty:
            st.info("暂无报名记录")
        else:
            st.subheader("📋 所有报名记录")
            st.dataframe(df, use_container_width=True)

            st.download_button("📥 下载Excel表格", 
                               df.to_csv(index=False, encoding="utf-8-sig"), 
                               "塘泽教育报名记录.csv")
            st.markdown("---")

            st.subheader("✏️ 修改 / 🗑 删除 单条记录")
            row_select = st.selectbox("选择要操作的记录序号", list(range(len(df))))
            row = df.iloc[row_select]

            with st.form("edit_form"):
                edit_name = st.text_input("姓名", value=row["姓名"])
                edit_phone = st.text_input("电话", value=str(row["电话"]))
                edit_course = st.selectbox("意向课程", 
                    ["办公应用", "平面设计", "视频制作", "产品建模", "室内设计", "机电绘图", "网页制作", "其他咨询"],
                    index=["办公应用", "平面设计", "视频制作", "产品建模", "室内设计", "机电绘图", "网页制作", "其他咨询"].index(row["意向课程"]))
                edit_level = st.radio("电脑基础", ["零基础", "有一点基础", "有一定基础"],
                    index=["零基础", "有一点基础", "有一定基础"].index(row["电脑基础"]))
                edit_remark = st.text_area("备注", value=row["备注"])

                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    save_edit = st.form_submit_button("✅ 保存修改")
                with col_btn2:
                    del_row = st.form_submit_button("🗑 删除本条记录")

            if save_edit:
                df.at[row_select, "姓名"] = edit_name
                df.at[row_select, "电话"] = str(edit_phone)
                df.at[row_select, "意向课程"] = edit_course
                df.at[row_select, "电脑基础"] = edit_level
                df.at[row_select, "备注"] = edit_remark
                save_sign_data(df)
                st.success("✅ 修改已保存！")
                st.rerun()

            if del_row:
                df = df.drop(row_select).reset_index(drop=True)
                save_sign_data(df)
                st.success("🗑 本条记录已删除！")
                st.rerun()

            st.markdown("---")
            st.subheader("⚠️ 危险操作")
            if st.button("🚮 清空所有报名记录", type="primary"):
                df_empty = pd.DataFrame(columns=["提交时间","姓名","电话","意向课程","电脑基础","备注"])
                save_sign_data(df_empty)
                st.warning("✅ 已清空全部记录！")
                st.rerun()

        if st.button("退出登录"):
            st.session_state.admin_logged_in = False
            st.session_state.edit_idx = None
            st.rerun()

# ----------------------
# 底部信息
# ----------------------
st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 联系我们")
st.sidebar.write("☎ 电话：020-82709166")
st.sidebar.write("🏫 地址：广州市增城区新塘镇")
st.sidebar.write("💻 塘泽教育 · 学会为止")
st.sidebar.write("📱 微信：同手机号")

st.markdown("---")
col_visit = st.columns([1, 2, 1])
with col_visit[1]:
    st.info(f"👀 网站累计访问人数：{count} 次")

st.markdown("© 2026 塘泽教育 版权所有")
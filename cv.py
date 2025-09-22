from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Crear documento
output_path = "Pablo_Dubourdieu_CV.pdf"
doc = SimpleDocTemplate(output_path, pagesize=A4, topMargin=20, bottomMargin=20)

# Estilos
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Heading", fontSize=12, leading=14, spaceAfter=6, textColor=colors.HexColor("#0B3954"), bold=True))
styles.add(ParagraphStyle(name="SubHeading", fontSize=11, leading=13, spaceAfter=4, textColor=colors.HexColor("#087E8B"), bold=True))
styles.add(ParagraphStyle(name="Body", fontSize=10, leading=12, spaceAfter=4))

elements = []

# Header
elements.append(Paragraph("<b>PABLO DUBOURDIEU</b> | Data Scientist | Economist", styles["Heading"]))
elements.append(Paragraph("Email: pablodub@gmail.com | Phone: (+598) 91 085 464 | GitHub: pablomdh | LinkedIn: pablo-dubourdieu", styles["Body"]))
elements.append(Spacer(1, 12))

# Profile
elements.append(Paragraph("<b>Profile</b>", styles["SubHeading"]))
profile_text = ("Data Scientist with a Master’s in Data Science and a Bachelor’s in Economics, specialized in large-scale ML models, "
                "data engineering, and applied analytics. Experienced in delivering predictive models and scalable data pipelines adopted "
                "by public institutions and the education technology sector. Skilled in Python, SQL, AWS, and Azure, with strong expertise "
                "in statistical modeling and applied analytics. Native Spanish speaker, fluent in English (C2), with basic knowledge of French (A2).")
elements.append(Paragraph(profile_text, styles["Body"]))
elements.append(Spacer(1, 12))

# Technical Skills
elements.append(Paragraph("<b>Technical Skills</b>", styles["SubHeading"]))
skills_text = ("<b>Core:</b> Python, SQL, ML, Spark, AWS, Docker<br/>"
               "<b>Complementary:</b> R, Tableau, Superset, Power BI, JavaScript, TypeScript, React<br/>"
               "<b>Methodologies:</b> SCRUM, Agile, PMI")
elements.append(Paragraph(skills_text, styles["Body"]))
elements.append(Spacer(1, 12))

# Work Experience
elements.append(Paragraph("<b>Work Experience</b>", styles["SubHeading"]))

work_experience = [
    ["Sr. Data Scientist / ML Engineer – Binsight", "10/2023 – Present",
     ["Trained classification models on imbalanced datasets.",
      "Implemented processing and validation pipelines in production, ensuring scalability and reproducibility.",
      "Generated automated reports and interactive visualizations to communicate results to non-technical clients.",
      "Spare Parts Demand Forecast (Ceibal): ML pipeline predicting stock needs per SKU with error metrics by family."]],
    
    ["Sr. Data Scientist – Uruguayan National Institute of Statistics (INE)", "05/2023 – Present",
     ["Designed and developed ETL processes for 50M+ administrative records, improving integration of heterogeneous data sources.",
      "Implemented validation procedures that reduced inconsistencies and strengthened statistical quality.",
      "Built classification models in Python to estimate resident population, providing key inputs for official statistics (AUC 0.84 vs. baseline 0.73).",
      "Developed dashboards in Tableau and Superset to support institutional decision-making.",
      "Led the parallel development of a chatbot in Azure."]],
    
    ["Software Developer – Oracle Netsuite", "11/2021 – 05/2023",
     ["Developed and implemented customized ERP solutions.",
      "Integrated programs with Netsuite, automated processes, created automated reports, and configured EFT payments."]],
    
    ["Financial & Economic Analyst – República Microfinanzas", "01/2018 – 02/2020",
     ["Conducted market and client analysis to support decision-making.",
      "Developed a credit scoring model using SQL, R, and Python.",
      "Automated reporting and operational processes across multiple areas, reducing dependency on IT.",
      "Delivered training sessions on process automation."]],
]

for job in work_experience:
    elements.append(Paragraph(f"<b>{job[0]}</b> &nbsp;&nbsp; ({job[1]})", styles["Body"]))
    for bullet in job[2]:
        elements.append(Paragraph(f"• {bullet}", styles["Body"]))
    elements.append(Spacer(1, 6))

# Education
elements.append(Paragraph("<b>Education</b>", styles["SubHeading"]))
education_text = ("<b>Master’s in Data Science</b> – UTEC & MIT, 2020–2022 (Thesis Defense Pending)<br/>"
                  "Thesis: Estimating the Resident Population in Uruguay using Administrative Records and Classification Models.<br/><br/>"
                  "<b>Bachelor’s in Economics</b> – Universidad de la República, 2013–2018")
elements.append(Paragraph(education_text, styles["Body"]))
elements.append(Spacer(1, 12))

# Other Courses
elements.append(Paragraph("<b>Other Courses</b>", styles["SubHeading"]))
courses_text = ("Full-Stack Web Development Bootcamp – Hack Academy, 2021<br/>"
                "Data Science for Sustainable Cities – UTEC, 2025<br/>"
                "TA in Python – UTEC, 2024<br/>"
                "TA in Data Science – INE, 2023")
elements.append(Paragraph(courses_text, styles["Body"]))
elements.append(Spacer(1, 12))

# Teaching
elements.append(Paragraph("<b>Teaching Experience</b>", styles["SubHeading"]))
teaching_text = ("SQL & Machine Learning Instructor – CPE Academy (2024 – Present)<br/>"
                 "Probability and Statistics Instructor – Universidad Católica (2023)")
elements.append(Paragraph(teaching_text, styles["Body"]))
elements.append(Spacer(1, 12))

# Languages
elements.append(Paragraph("<b>Languages</b>", styles["SubHeading"]))
languages_text = ("Spanish – Native<br/>English – C2 (Proficiency)<br/>French – A2 (Basic)<br/>Portuguese – Basic (Conversational)")
elements.append(Paragraph(languages_text, styles["Body"]))

# Construir PDF
doc.build(elements)
output_path

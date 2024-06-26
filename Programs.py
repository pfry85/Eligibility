import streamlit as st

def streamlist(gender, age, department, insurance_coverage, needs_transportation, is_asylum_seeker_or_venezuelan):
    available_programs = []

    # General rules for males
    if gender == "Male":
        if age >= 18:
            available_programs.extend([
                "American Cancer Society (ACS)",
                "FPP"
            ])
        if needs_transportation:
            available_programs.append("Hamman Foundation")
        return available_programs

    # General rules for females
    if gender == "Female":
        if age >= 0 and age <= 11:
            if needs_transportation:
                available_programs.append("Hamman Foundation")
            return available_programs  # No other programs available
        elif age >= 12 and age <= 17:
            available_programs.append("Charity Guild of Catholic Women (RAAPs)")
            if needs_transportation:
                available_programs.append("Hamman Foundation")
            return available_programs
        elif age >= 18:
            available_programs.extend([
                "FPP",
                "Junior League of Houston",
                "Houston Methodist In Kind Grant",
                "American Cancer Society (ACS)",
                "HTW",
                "Breast Health Programs",
                "American Cancer Society (3YR)",
                "Charity Guild of Catholic Women",
                "Good Rx",
                "Rockwell Fund"
            ])
            if needs_transportation:
                available_programs.append("Hamman Foundation")
            if is_asylum_seeker_or_venezuelan:
                available_programs.append("Simon Bolivar")
            return available_programs

    # Department-specific rules
    if department == "OBGYN":
        available_programs.extend([
            "American Cancer Society (ACS)",
            "HTW",
            "Breast Health Programs",
            "American Cancer Society (3YR)",
            "Charity Guild of Catholic Women",
            "Good Rx",
            "Rockwell Fund"
        ])
        if needs_transportation:
            available_programs.append("Hamman Foundation")
        if is_asylum_seeker_or_venezuelan:
            available_programs.append("Simon Bolivar")
        return available_programs

    if department == "Pediatrics":
        available_programs.append("Charity Guild of Catholic Women (RAAPs)")
        if needs_transportation:
            available_programs.append("Hamman Foundation")
        return available_programs

    if department == "Family/Internal Med":
        available_programs.extend([
            "AHA",
            "American Cancer Society (ACS)",
            "Breast Health Women"
        ])
        if needs_transportation:
            available_programs.append("Hamman Foundation")
        return available_programs

    # Insurance-specific rules
    if insurance_coverage == "Uninsured":
        available_programs.extend([
            "American Cancer Society (ACS)",
            "HTW",
            "Breast Health Programs",
            "American Cancer Society (3YR)",
            "Charity Guild of Catholic Women (RAAPs)",
            "Charity Guild of Catholic Women",
            "Good Rx",
            "Junior League of Houston",
            "Houston Methodist In Kind Grant",
            "Rockwell Fund"
        ])
        if is_asylum_seeker_or_venezuelan:
            available_programs.append("Simon Bolivar")
    else:
        available_programs.extend([
            "Junior League of Houston",
            "Charity Guild of Catholic Women",
        ])

    # Add Hamman Foundation if transportation is needed or for all females ages 0 to 11
    if needs_transportation or (gender == "Female" and age >= 0 and age <= 11):
        available_programs.append("Hamman Foundation")

    return available_programs

def program_details(program):
    details = {
        "FPP": "Physical or WWE, Contraception, & BP Follow Ups",
        "HTW": "WWE, Birth Control",
        "Breast Health Programs": "Breast cancer screening for patients that do not qualify for Projet Valet",
        "American Cancer Society (ACS)": "FIT Test",
        "American Cancer Society (3YR)": "Blood pressure management & food distribution",
        "Charity Guild of Catholic Women (RAAPs)": "ADO depression prevention screening",
        "Charity Guild of Catholic Women": "BAM & Nutrition Support for pregnant women",
        "Junior League of Houston": "BAM & Nutrition Support for pregnant women",
        "Houston Methodist In Kind Grant": "Covers lab charges for patients at NAM & West Houston",
        "Rockwell Fund": "WWE",
        "Simon Bolivar": "WWE for asylum seeking women or Venezuelan",
        "Good Rx": "Contraception",
        "Hamman Foundation": "Uber Health Transportation"
    }
    return details.get(program, "No details available for this program.")

def main():
    st.title("SBCHC Patient Programs")

    gender = st.selectbox("Select Gender", ["Male", "Female"])
    age = st.number_input("Enter Age", min_value=0, step=1)
    department = st.selectbox("Select Department", ["OBGYN", "Pediatrics", "Family/Internal Med"])
    insurance_coverage = st.selectbox("Insurance Coverage", ["Insured", "Uninsured"])
    needs_transportation = st.radio("Does the patient need transportation?", ["Yes", "No"], index=1)
    is_asylum_seeker_or_venezuelan = st.radio("Is the patient an asylum seeker or Venezuelan?", ["Yes", "No"], index=1) == "Yes"

    if st.button("Check Eligibility"):
        available_programs = streamlist(gender, age, department, insurance_coverage, needs_transportation == "Yes", is_asylum_seeker_or_venezuelan)
        if available_programs:
            st.sidebar.title("Available Programs")
            for idx, program in enumerate(available_programs, start=1):
                with st.sidebar.expander(f"{idx}. {program}"):
                    st.write(program_details(program))
        else:
            st.warning("No programs available for the selected criteria.")

if __name__ == "__main__":
    main()

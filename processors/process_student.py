from pathlib import Path
import docx2txt as d2t
from pydantic import BaseModel
from typing import Optional, Self
import json
import re

class ParseStudent(BaseModel):
    student_name: str
    is_contact_person: bool
    student_phone: Optional[str]
    student_email: Optional[str]
    group_number: str
    property_one: Optional[str]
    property_two: Optional[str]
    property_three: Optional[str]
    current_address: Optional[str]
    gpa: Optional[str]
    greek_life: Optional[str]

    @staticmethod
    def read_docx(docx_path: Path) -> str:
        return d2t.process(str(docx_path))

    def process_data(self, data: str) -> Self:
        # Delegate to the classmethod which returns a validated instance
        return self.__class__.from_text(data)

    @classmethod
    def from_text(cls, data: str) -> Self:
        def extract_field(text: str, labels, stop_labels=None) -> Optional[str]:
            if isinstance(labels, str):
                labels = [labels]
            stop_labels = stop_labels or []
            label_pattern = r"|".join(re.escape(label) for label in labels)
            stop_pattern = r"|".join(re.escape(label) for label in stop_labels)
            if stop_pattern:
                pattern = rf"(?:{label_pattern})\s*[:\-]?\s*(.*?)(?=\s*(?:{stop_pattern})(?:\s*[:\-]|\s|$))"
            else:
                pattern = rf"(?:{label_pattern})\s*[:\-]?\s*(.*)"
            match = re.search(pattern, text, flags=re.I | re.S)
            if not match:
                return None
            value = match.group(1).strip()
            return value if value else None

        try:
            student_first_name = extract_field(
                data,
                ["Name:"],
                stop_labels=["Middle:", "Last:", "Cell Phone Number:"]
            )
            student_middle_name = extract_field(
                data,
                ["Middle:"],
                stop_labels=["Last:", "Cell Phone Number:"]
            )
            student_last_name = extract_field(
                data,
                ["Last:"],
                stop_labels=["Cell Phone Number:", "Email:"]
            )
            contact_person_raw = extract_field(
                data,
                ["Contact Person of Group:"],
                stop_labels=["List Others in Group:", "Student Information"]
            )
            student_phone = extract_field(
                data,
                ["Cell Phone Number:"],
                stop_labels=["Email:", "Date of Birth:", "Social Security #:"]
            )
            student_email = extract_field(
                data,
                ["Email:"],
                stop_labels=["Date of Birth:", "Social Security #:", "Drivers License #:"]
            )
            property_one = extract_field(
                data,
                ["1st Choice:"],
                stop_labels=["2nd Choice:", "3rd Choice:", "Contact Person of Group"]
            )
            property_two = extract_field(
                data,
                ["2nd Choice:"],
                stop_labels=["3rd Choice:", "Contact Person of Group:", "List Others in Group:"]
            )
            property_three = extract_field(
                data,
                ["3rd Choice:"],
                stop_labels=["Contact Person of Group:", "List Others in Group:", "Student Information"]
            )
            current_address = extract_field(
                data,
                ["Current Address:"],
                stop_labels=["City:", "State:", "Zip:"]
            )
            gpa = extract_field(
                data,
                ["Cumulative GPA:"],
                stop_labels=["Are You Involved In URI Athletics?", "If yes, which sports?"]
            )
            greek_life = extract_field(
                data,
                ["If so, which one?"],
                stop_labels=["Student Academic Information", "What Year Are You In School?"]
            )
        except Exception as e:
            raise e(f"Error: {e}")

        student_full_name = student_first_name + " " + student_middle_name +  " " + student_last_name
        contact_person_bool = True if student_first_name and student_last_name in contact_person_raw else False

        return cls(
            student_name=student_full_name,
            is_contact_person=contact_person_bool,
            student_phone=student_phone,
            student_email=student_email,
            group_number="",
            property_one=property_one,
            property_two=property_two,
            property_three=property_three,
            current_address=current_address,
            gpa=gpa,
            greek_life=greek_life,
        )

    @classmethod
    def from_docx(cls, docx_path: Path) -> Self:
        text = cls.read_docx(docx_path)
        return cls.from_text(text)

        

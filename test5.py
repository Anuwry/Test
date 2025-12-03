class Course:
    def __init__(self, code, name, max_seats):
        self.code = code
        self.name = name
        self.max_seats = max_seats
        self.students = []
    
    def get_price(self):
        return 1500
    
    def enroll(self, student_name):
        if len(self.students) == self.max_seats:
            print("คอร์สเต็มแล้ว")
            return False
        if student_name in self.students:
            print("คุณลงทะเบียนวิชานี้ไปแล้ว")
            return False
        
        self.students.append(student_name)
        print("ลงทะเบียนสำเร็จ")
        return True
    
    def get_status(self):
        return f"{self.name} ({len(self.students)}/{self.max_seats} seats)"
    
class Workshop(Course):
    def get_price(self):
        return 2500
    
class Seminar(Course):
    def get_price(self):
        return 0

class School:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
    
    def show_courses(self):
        print(f"\n--- 📚 คอร์สที่เปิดสอน: {self.name} ---")
        for c in self.courses:
            print(f"- [{c.code}] {c.get_status()} | ราคา: {c.get_price()} บาท")
        print("-" * 30)
    
    def register_student(self, student_name, course_code):
        print(f"🔄 นักเรียน {student_name} กำลังขอลงทะเบียนวิชา {course_code}...")
        for b in self.courses:
            if b.code == course_code:
                success = b.enroll(student_name)
                if success:
                    price = b.get_price()
                    print(f"ยอดที่ต้องชำระ {price} บาท")
                return
            
        print("ไม่พบรหัสวิชา")

if __name__ == "__main__":
    school = School("Code Academy")

    # สร้างคอร์ส (สังเกต max_seats)
    c1 = Course("CS101", "Python Basics", 2)      # รับแค่ 2 คน
    c2 = Workshop("WS200", "Robot Building", 5)   # รับ 5 คน
    c3 = Seminar("SEM99", "Tech Trends 2025", 50) # รับ 50 คน

    school.add_course(c1)
    school.add_course(c2)
    school.add_course(c3)

    school.show_courses()

    # 1. ลงทะเบียนปกติ
    school.register_student("Somchai", "CS101") # เสีย 1500
    school.register_student("Alice", "WS200")   # เสีย 2500
    school.register_student("Bob", "SEM99")     # ฟรี

    # 2. ลงทะเบียนซ้ำ (ต้อง Error)
    school.register_student("Somchai", "CS101") 

    # 3. ลงทะเบียนตอนคอร์สเต็ม (ต้อง Error)
    school.register_student("Ken", "CS101") # เข้าเป็นคนที่ 2 (ได้)
    school.register_student("Ryu", "CS101") # เข้าเป็นคนที่ 3 (เต็ม!)

    # 4. ลงทะเบียนวิชาทิพย์ (ต้อง Error)
    school.register_student("Somchai", "MUA999")

    # ดูยอดคงเหลือ
    school.show_courses()
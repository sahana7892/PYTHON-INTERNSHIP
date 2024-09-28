class TrainingSession:
    def _init_(self, session_id: str, title: str, coach: str, duration: float, level: str):
        self.session_id = session_id
        self.title = title
        self.coach = coach
        self.duration = duration
        self.level = level

    def _str_(self) -> str:
        return f"Session ID: {self.session_id}, Title: {self.title}, Coach: {self.coach}, Duration: {self.duration}h, Level: {self.level}"


class TrainingProgram:
    def _init_(self, program_id: str, description: str):
        self.program_id = program_id
        self.description = description
        self.sessions = []

    def add_session(self, session: TrainingSession) -> None:
        self.sessions.append(session)

    def remove_session(self, session_id: str) -> None:
        self.sessions = [s for s in self.sessions if s.session_id != session_id]

    def get_sessions(self) -> list:
        return self.sessions

    def _str_(self) -> str:
        return f"Program ID: {self.program_id}, Description: {self.description}, Sessions: {len(self.sessions)}"


class ScheduleManager:
    def _init_(self):
        self.programs = {}

    def add_program(self, program: TrainingProgram) -> None:
        self.programs[program.program_id] = program

    def delete_program(self, program_id: str) -> None:
        if program_id in self.programs:
            del self.programs[program_id]

    def get_program(self, program_id: str) -> TrainingProgram:
        return self.programs.get(program_id, None)


class AttendanceManager:
    def _init_(self):
        self.attendance = {}

    def record_attendance(self, session_id: str, attendees: list) -> None:
        self.attendance[session_id] = attendees

    def get_attendance(self, session_id: str) -> list:
        return self.attendance.get(session_id, [])


def main():
    schedule_manager = ScheduleManager()
    attendance_manager = AttendanceManager()

    while True:
        print("\nMenu:")
        print("1. Add Training Program")
        print("2. Add Session to Program")
        print("3. View Sessions in Program")
        print("4. Remove Session from Program")
        print("5. Record Attendance")
        print("6. View Attendance")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            program_id = input("Enter Program ID: ")
            description = input("Enter Program Description: ")
            program = TrainingProgram(program_id, description)
            schedule_manager.add_program(program)
            print("Program added successfully!")

        elif choice == '2':
            program_id = input("Enter Program ID to add session: ")
            program = schedule_manager.get_program(program_id)
            if program:
                session_id = input("Enter Session ID: ")
                title = input("Enter Session Title: ")
                coach = input("Enter Coach Name: ")
                duration = float(input("Enter Duration (in hours): "))
                level = input("Enter Difficulty Level: ")
                session = TrainingSession(session_id, title, coach, duration, level)
                program.add_session(session)
                print("Session added successfully!")
            else:
                print("Program not found!")

        elif choice == '3':
            program_id = input("Enter Program ID to view sessions: ")
            program = schedule_manager.get_program(program_id)
            if program:
                sessions = program.get_sessions()
                for session in sessions:
                    print(session)
            else:
                print("Program not found!")

        elif choice == '4':
            program_id = input("Enter Program ID to remove session from: ")
            program = schedule_manager.get_program(program_id)
            if program:
                session_id = input("Enter Session ID to remove: ")
                program.remove_session(session_id)
                print("Session removed successfully!")
            else:
                print("Program not found!")

        elif choice == '5':
            session_id = input("Enter Session ID to record attendance: ")
            attendees = input("Enter attendee names (comma separated): ").split(',')
            attendance_manager.record_attendance(session_id, [attendee.strip() for attendee in attendees])
            print("Attendance recorded successfully!")

        elif choice == '6':
            session_id = input("Enter Session ID to view attendance: ")
            attendees = attendance_manager.get_attendance(session_id)
            if attendees:
                print("Attendees:", ", ".join(attendees))
            else:
                print("No attendance recorded for this session.")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == '_main_':
    main()
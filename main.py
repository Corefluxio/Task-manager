class Task:
    def __init__(self,title):
        self.title = title
        self.is_completed = False
    
    
    def mark_completed(self):
     self.is_completed = True
    
    def __str__(self):
       if self.is_completed:
          return f"[✅] {self.title}"
       else:
          return f"[❌] {self.title}"
    

class TaskManager:
    def __init__(self):
      self.tasks = []
    
    def add_task(self,title):
       self.tasks.append(Task(title))
       return "Задача добавлена"
    
    def show_tasks(self):
        if not self.tasks:
            print("Нет задач")
            return
        
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
    
    def delete_task(self,index):
       if 0 < index <= len(self.tasks):
           del self.tasks[index - 1]
           return 'Задача удалена'
       else:
          return 'Номер задачи введен неправильно'
       
    def mark_task_completed(self,index):
       if 0 < index <= len(self.tasks):
             self.tasks[index - 1].mark_completed()
             return "Задача отмечена как выполненная"
       else:
          return 'Номер задачи введен неправильно'
    
    def save_to_file(self):
       with open("tasks.txt", "w") as f:
          for task in self.tasks:
             f.write(f'{task.title}|{task.is_completed}\n')
       
    def load_from_file(self):
     self.tasks = []
     try:
       with open("tasks.txt", "r") as f:
        for line in f:
             title, status = line.strip().split("|")
             task = Task(title)
             if status == 'True':
               task.mark_completed()
             self.tasks.append(task)
     except FileNotFoundError:
         with open("tasks.txt", "x") as f:
            pass
            
manager = TaskManager()
manager.load_from_file()

while True:
    print("\n--- МЕНЮ ---")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Отметить задачу выполненной")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите задачу: ")
        print(manager.add_task(title))
        

    elif choice == "2":
        manager.show_tasks()

    elif choice == "3":
        manager.show_tasks()
        try:
            index = int(input("Введите номер задачи для удаления: "))
            print(manager.delete_task(index))
        except ValueError:
            print("Нужно ввести число")

    elif choice == "4":
        manager.show_tasks()
        try:
            index = int(input("Введите номер выполненной задачи: "))
            print(manager.mark_task_completed(index))
        except ValueError:
            print("Нужно ввести число")

    elif choice == "5":
        manager.save_to_file()
        print("Задачи сохранены. Выход из программы.")
        break

    else:
        print("Неправильный выбор, попробуйте снова")
    






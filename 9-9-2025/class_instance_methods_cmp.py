class Book:
    # 类属性：所有实例共享，记录总数量
    total_books = 0

    def __init__(self, title):
        # 实例属性：每个实例独有的数据
        self.title = title
        Book.total_books += 1  # 每创建一个实例，总数量+1

    # 实例方法：操作实例自身的数据
    def get_title(self):
        return f"书名：{self.title}"

    # 类方法：操作类的数据（类属性）
    @classmethod
    def get_total(cls):
        return f"总藏书量：{cls.total_books} 本"


# 使用实例方法：必须先创建实例
book1 = Book("Python入门")
print(book1.get_title())  # 输出：书名：Python入门

# 使用类方法：直接通过类名调用（无需创建实例）
print(Book.get_total())  # 输出：总藏书量：1 本

# 再创建一个实例
book2 = Book("Java实战")
print(book2.get_title())  # 输出：书名：Java实战
print(Book.get_total())   # 输出：总藏书量：2 本
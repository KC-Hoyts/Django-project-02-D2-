import datetime
import time
best_post ={'date_creation': datetime.datetime(2023, 4, 25, 15, 14, 44, 66071), 'author': 2, 'rating': 3, 'title': 'Вторая статья!'}
print(best_post)

while True:
    print(f"Дата создания: {str(best_post['date_creation'])[:19]}")
    print(f"Автор: {best_post['author']}")
    print(f"Рейтинг поста: {best_post['rating']}")
    print(f"Заголовок: {best_post['title']}")

    break



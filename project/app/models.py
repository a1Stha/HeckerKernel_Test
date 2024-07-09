from django.db import models

# Create your models here.

# From django.db import models

Task = {
	"Pending":"pending",
	"Done":"done",
}
class Task(models.Model):
	task_details=models.TextField(max_length=50)
	task_type= models.CharField(max_length=50 , choices=Task)
	def __str__(self):
		return (self.task_details)
class User(models.Model):
	Name=models.CharField(max_length=50)
	Email=models.EmailField(max_length=50)
	Mobile=models.IntegerField()
	ID = models.AutoField(primary_key=True)
	Task = models.ForeignKey(Task,on_delete=models.CASCADE,null=True)
	class Meta:
		db_table= 'User'
	def __str__(self):
		return  self.Name











# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=15)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class Task(models.Model):
#     PENDING = 'Pending'
#     DONE = 'Done'
#     TASK_CHOICES = [
#         (PENDING, 'Pending'),
#         (DONE, 'Done'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task_detail = models.TextField()
#     task_type = models.CharField(max_length=20, choices=TASK_CHOICES, default=PENDING)

#     def __str__(self):
#         return self.task_detail











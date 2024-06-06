

class Employee:
    # class attribute to track current number of employees
    employee_count = 0
    
    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email and hire date. 
        Adjusts the employee_count class attribute when a new employee 
        is created. 
        """
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        # Initialize an empty array
        self.posts = []
        # Initializes an empty list to hold all comments
        self.comments = [] 

    # method to create Post object that contains the author
    # and message
    def post_message(self, message):
        post = Post(self, message)
        self.posts.append(post)
        return post
    
    # method to create the comment object on the Post
    def comment_on_post(self, message, post):
        """
        Method to create a new comment on a post 
        Creates a new Comment object with a message, Employee as author, and
        the given post. Appends the comment object to the author Employee's 
        comment list and the list of comments on the post. 
        """
        comment = Comment(self, message, post)
        post.comments.append(comment) #appends comment to the post object
        self.comments.append(comment) # appends comment to the Employee object
        return comment


    # Employee object toString method.
    def __str__(self):
        return f"Employee : {self.name} \nHire Date : {self.hire_date}"

class Post:
    def __init__(self, author, message):
        '''
        Constructor method for Post class that initializes a Post object
        with author , message and emply comments list to hold the comments.
        '''
        self.author = author
        self.message = message
        self.comments = []

    def edit_message(self, new_message):
        self.message = new_message

e1 = Employee("Dilawar", "s@s.com", "09/13/2021")
e1.post_message("Helloooo everyone....")
print(e1.posts)
print(e1)

# Comment class
class Comment:
    def __init__(self, author, message, post):
        """
        Constructor method for Comment class
        Initializes a Comment object with an author Employee, a message, and a
            Post object
        """
        self.author = author
        self.message = message
        self.post = post

    def edit_message(self, new_message):
        """
        Method to edit the message of a comment
        Updates the message attribute of the comment object
        """
        self.message = new_message

"""
Try out methods and attributes
"""
# create a new employee
e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")
e2 = Employee("Pat Candella", "pat.candella@example.com", "12/1/2022")

# Use the post message method to create new Post objects
intro_message = e2.post_message("Hi all! So excited to be joining" 
+ " the company!")

# Use the returned post to comment on the message
e1.comment_on_post("Welcome to the team!", intro_message)
e2.comment_on_post("Thanks!", intro_message)


# Another example of a new post with comment exchange
workshop_post = e1.post_message("I just attended a workshop.")

e2.comment_on_post("Cool! What was the workshop about?", workshop_post)
e1.comment_on_post("Python classes and objects", workshop_post)

print ("Mary's posts are",[post.message for post in e1.posts])
print ("Pat's posts are", [post.message for post in e2.posts])

print ("-" * 50)

print ("Mary's comments are",[comment.message for comment in e1.comments])
print ("Pat's comments are",[comment.message for comment in e2.comments])

print ("-" * 50)

print ("Intro message comments are",[comment.message for comment in intro_message.comments])
print ("Workshop post comments are", [comment.message for comment in workshop_post.comments])

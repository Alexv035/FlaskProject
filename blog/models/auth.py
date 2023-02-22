class Author(db.Model):
    def __str__(self):
        return self.user.username

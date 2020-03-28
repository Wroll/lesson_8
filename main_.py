import mongoengine as ME

ME.connect('TestUsers', host='127.0.0.1', port=27017)


class User(ME.Document):
    name = ME.StringField(min_length=2, max_length=255)
    login = ME.StringField(max_length=255, min_length=3)
    password = ME.StringField(min_length=10, max_length=1024)
    insteres = ME.ListField(ME.StringField())

    def __str__(self):
        return f'{self.id} {self.name}'


if __name__ == '__main__':
    user = User(name='John', login='John', password='John123454566', insteres=['Footbol'])
    user.save()

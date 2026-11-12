class Blog:
    def __init__(self, comments):
        self.comments = comments

def test_blog():
    blog = Blog(['comment1', 'comment2'])
    assert len(blog.comments) == 2
    assert blog.comments[0] == 'comment1'
    assert blog.comments[1] == 'comment2'

def test_question_comprehended():
    blogs = [
        Blog(['123', '1234']),
        Blog(['1', '12', '123456']),
    ]

    def someFunction(comment):
        return len(comment)

    result = [[someFunction(comment) for comment in blog.comments] for blog in blogs]

    # for blog in blogs:
    #     inner = []
    #     for comment in blog.comments:
    #         inner.append(someFunction(comment))
    #     result.append(inner)

    assert len(result) == 2
    assert len(result[0]) == 2
    assert len(result[1]) == 3

    assert result[0] == [3, 4]
    assert result[1] == [1, 2, 6]

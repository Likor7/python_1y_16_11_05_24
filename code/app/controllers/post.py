from app.models import Post


class PostController:
    @staticmethod
    def get_posts():
        return Post.query.all()

    @staticmethod
    def create_post(title: str, content: str, user_id: int):
        post = Post(title=title, content=content, user_id=user_id)
        post.save()

    @staticmethod
    def get_post_by_id(post_id: int):
        return Post.query.get(post_id)

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get(post_id)
        if post:
            post.delete()

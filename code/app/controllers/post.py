from app.models import Post


class PostController:
    def get_posts():
        return Post.query.all()

    def create_post(title: str, content: str, user_id: int):
        post = Post(title=title, content=content, user_id=user_id)
        post.save()

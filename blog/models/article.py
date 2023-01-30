from blog.models.article_tag import article_tag_association_table


class Article(db.Model):

    tags = relationship("Tag",
                        secondary=article_tag_association_table,
                        back_populates="articles",
                        )

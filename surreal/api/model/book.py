from ma import mapper

# Book API model
class BookSchema(mapper.Schema):
    id = mapper.String()
    title = mapper.String()
    content = mapper.String()
    published_at = mapper.DateTime(dump_to = 'publishedAt')
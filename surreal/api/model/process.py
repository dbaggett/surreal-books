from typing import Dict
from ma import mapper
from surreal.service.model.process import ProcessStatus

# Process API model
class Process(mapper.Schema):
    id: mapper.String()
    status: mapper.String()
    requested_at: mapper.DateTime(dump_to = 'requestedAt')
    started_at: mapper.DateTime(dump_to = 'startedAt')
    finished_at: mapper.DateTime(dump_to = 'finishedAt')
    user_input: mapper.String(dump_to = 'userInput')
    links = mapper.Method('generate_links')

    # Generates HATEOAS links to this resource and the generated book, if available (status=PUBLISHED)
    def generate_links(self, obj) -> Dict:
        if obj.status is ProcessStatus.PUBLISHED:
            return {
                "self": f"/api/processes/{self.id}",
                "book": f"/api/books/{obj.book_id}"
            }
        else:
            return {
                "self": f"/api/processes/{self.id}"
            }

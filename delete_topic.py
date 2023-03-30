from google.cloud import pubsub_v1

# TODO(developer)
project_id = "datamigrationdf20may"
topic_id = "csv_test"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

publisher.delete_topic(request={"topic": topic_path})

print(f"Topic deleted: {topic_path}")
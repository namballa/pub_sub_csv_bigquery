
from concurrent import futures
from google.cloud import pubsub_v1
from typing import Callable
import requests as rq
from contextlib import closing

# TODO(developer)
project_id = "datamigrationdf20may"
topic_id = "csv_test"
url = "https://data.kingcounty.gov/api/views/yaai-7frk/rows.csv?accessType=DOWNLOAD"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)
publish_futures = []

def get_callback(
    publish_future: pubsub_v1.publisher.futures.Future, data: str
) -> Callable[[pubsub_v1.publisher.futures.Future], None]:
    def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
        try:
            # Wait 60 seconds for the publish call to succeed.
            print(publish_future.result(timeout=60))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out.")

    return callback
with closing(rq.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    flag = 0
    print(f)
    for row in f:
        if flag == 0:
            flag = 1
            pass # skip header row
        else:
             publish_future = publisher.publish(topic_path, data=row.encode('utf-8'))
            # Non-blocking. Publish failures are handled in the callback function.
             publish_future.add_done_callback(get_callback(publish_future, data=row.encode('utf-8')))
             publish_futures.append(publish_future)
             # Wait for all the publish futures to resolve before exiting.
             futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)

             print(f"Published messages with error handler to {topic_path}.")

  
   
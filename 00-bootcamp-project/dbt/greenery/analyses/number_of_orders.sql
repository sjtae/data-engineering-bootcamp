select
    count(*) as order_record_count
from {{ ref('stg_greenery__orders') }}
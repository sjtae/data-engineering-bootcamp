select
    count(*) as record_count
from {{ ref('stg_greenery__users') }}
with

dim_events as (

    select * from {{ ref('stg_greenery__events') }}

)

select * from dim_events

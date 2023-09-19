with fct as (
    select * from {{ ref('fct_movements') }}
),
trains_that_never_late_and_off_route as (
    select
        train_id,
        array_agg(variation_status) as variation_status
    from fct 
    group by 1
),
unnest_trains_that_never_late_and_off_route as (
    select
        distinct(train_id) 
    from trains_that_never_late_and_off_route, unnest(variation_status) as status
    where status not in ("LATE","OFF ROUTE")
)

select * from unnest_trains_that_never_late_and_off_route

-- with a as (
--     select ["current", "previous", "birth"] as address_history
-- )

-- select addr
-- from
--   a
--   , unnest(address_history) as addr
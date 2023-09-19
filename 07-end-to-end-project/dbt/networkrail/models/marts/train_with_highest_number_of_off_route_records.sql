with fct as (
    select * from {{ ref('fct_movements') }}
),
train_with_highest_number_of_off_route as (
    select 
        train_id,
        toc_id,
        company_name,
        count(*) off_route_record 
    from fct 
    where variation_status = "OFF ROUTE"
    group by 1, 2, 3
    order by 4 desc
    limit 5
)
select * from train_with_highest_number_of_off_route
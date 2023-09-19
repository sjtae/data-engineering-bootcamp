with fct as (
    select * from {{ ref('fct_movements') }}
),
operating_company_with_the_highest_num_of_on_time_trains as (
    select
        company_name,
        count(*) as on_time_trains_record
    from fct
    where variation_status = "ON TIME"
    group by 1
    order by 2 desc
    limit 1
)
select * from operating_company_with_the_highest_num_of_on_time_trains
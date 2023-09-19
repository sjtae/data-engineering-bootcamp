with fct as (
    select * from {{ ref('fct_movements') }}
),
operating_company_with_the_highest_num_of_late_trains as (
    select
        company_name,
        variation_status,
        count(*) as late_trains_record
    from fct
    where variation_status = "LATE"
    group by 1,2
    order by 3 desc
    limit 1
)
select * from operating_company_with_the_highest_num_of_late_trains
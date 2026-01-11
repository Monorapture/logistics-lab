DROP VIEW IF EXISTS view_event_log;

CREATE VIEW view_event_log AS 
    Select
    p.sku  as '_CASE_KEY',
    m.movement_date as '_EVENTTIME',
    CASE
        WHEN m.movement_type = 'INBOUND' THEN 'Goods Receipt'
        WHEN m.movement_type = 'OUTBOUND' THEN 'Goods Issue'
        WHEN m.movement_type = 'RETURN' Then 'Return Inward'
        ELSE 'Unknown Activity'
    END AS '_ACTIVITY_MAIN',
    ROW_NUMBER() OVER (
    PARTITION BY p.sku   -- Für wen fängt der Zähler neu an? (Pro Produkt/SKU)
    ORDER BY m.movement_date        -- Wonach wird sortiert? (Zeit)
) as "_SORTING"
FROM products p
LEFT JOIN inventory_movements m ON p.product_id = m.product_id;



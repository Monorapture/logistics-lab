SELECT 
    p.name as product_id,
    p.sku,
IFNULL(SUM(CASE
        WHEN m.movement_type = 'INBOUND' THEN m.quantity
        WHEN m.movement_type = 'RETURN' THEN m.quantity
        WHEN m.movement_type = 'OUTBOUND' THEN -1 * m.quantity
        ELSE 0
    END), 0) as current_stock_level
FROM products p
LEFT JOIN inventory_movements m ON m.product_id = p.product_id
GROUP BY p.name, p.sku
ORDER BY current_stock_level DESC;

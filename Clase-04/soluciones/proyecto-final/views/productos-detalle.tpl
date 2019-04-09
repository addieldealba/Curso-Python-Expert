%rebase("base.tpl", title="Detalle")

    <h2>Detalle de producto</h2>
    <hr />
    <div class="detalle">
        <div class="producto">
            <ul class="datos">
                <li><strong>Nombre:</strong> {{producto.nombre}}</li>
                <li><strong>Cantidad:</strong> {{producto.cantidad}}</li>
                <li><strong>Precio:</strong> ${{producto.precio_str}}</li>
            </ul>
            <aside>
                <img src="/imagenes/{{producto.imagen}}" alt="Foto de {{producto.nombre}}" />
            </aside>
        </div>
    </div>

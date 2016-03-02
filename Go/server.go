package main


import "github.com/gin-gonic/gin"

func main() {
    // = es asignacion, : es declaracion
    //gin, levanta un servidor en HTTP.
    //ejecuta la funcion al recibir una llamada

    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200,gin.H{
            "message":"pong",
        })
    })
    r.Run()
}

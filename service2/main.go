package main

import (
	"math/rand"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

// Define a struct for the sayings response
type SayingResponse struct {
	Saying string `json:"saying"`
}

// Define a struct for the health check response
type HealthCheckResponse struct {
	Status string `json:"status"`
}

func main() {
	e := echo.New()

	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: []string{"*"},  // Specify domains in production
		AllowMethods: []string{echo.GET, echo.POST, echo.PUT, echo.PATCH, echo.DELETE},
	}))
	

	// Taoist or Buddhist sayings endpoint
	e.GET("/sayings", func(c echo.Context) error {
		sayings := []string{
			"The journey of a thousand miles begins with one step. - Lao Tzu",
			"Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
			"Knowing others is intelligence; knowing yourself is true wisdom. - Lao Tzu",
			"Peace comes from within. Do not seek it without. - Buddha",
		}
		// Randomly return one of the sayings
		index := rand.Intn(len(sayings))
		response := SayingResponse{
			Saying: sayings[index],
		}
		return c.JSON(http.StatusOK, response)
	})

	e.GET("/healthy", func(c echo.Context) error {
		response := HealthCheckResponse{
			Status: "OK",
		}
		return c.JSON(http.StatusOK, response)
	})

	e.Logger.Fatal(e.Start(":9000"))
}

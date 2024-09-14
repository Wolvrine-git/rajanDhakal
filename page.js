"use client"
import React, { useEffect, useState } from 'react'

const page = () => {
  const [sec, setsec] = useState(0)
  const [min, setmin] = useState(0)
  const [hour, sethour] = useState(0)

  useEffect(() => {
    setInterval(() => {
      let currenttime = new Date()
      let h = currenttime.getHours()
      let m = currenttime.getMinutes()
      let s = currenttime.getSeconds()
      setsec(s / 60 * 360)
      setmin(m / 60 * 360)
      sethour(h / 12 * 360)
    }, 1000)
  }, [])
  return (
    <>
      <div className="container h-screen bg-[#ecf0f1] w-screen flex justify-center items-center">
        <div className="box bg-white h-[60vh] w-[60vh] rounded-full  flex justify-center items-center shadow-lg relative border-[40px]">
          <div className="point bg-[#000] relative h-5 w-5 rounded-full flex justify-center items-center ">
            <div className="handle bg-[black] h-32 w-1  absolute origin-bottom bottom-1/2 rounded-xl " style={{ transform: `rotate(${sec}deg)` }}></div>
            <div className="handle bg-[black] h-28 w-1  absolute origin-bottom bottom-1/2 rounded-2xl" style={{ transform: `rotate(${min}deg)` }}></div>
            <div className="handle bg-[black] h-20 w-1  absolute origin-bottom bottom-1/2 rounded-xl" style={{ transform: `rotate(${hour}deg)` }}></div>
          </div>
          <div className="time absolute top-0 p-4 text-2xl">
            12
          </div>
          <div className="time absolute bottom-0 p-4 text-2xl">
            6
          </div>
          <div className="time absolute left-0 p-4 text-2xl">
            9
          </div>
          <div className="time absolute right-0 p-4 text-2xl">
            3
          </div>
        </div>
      </div>
    </>
  )
}

export default page
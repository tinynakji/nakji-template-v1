// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import axios from 'axios'

type Data = {
  users: string
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  const usersRes = await fetch(
    process.env.API_PATH + "/api/v1/users",
    {
      method: "GET"
    }
  )
  const users = await usersRes.json()
  res.status(200).json({ users: String(users) })
}

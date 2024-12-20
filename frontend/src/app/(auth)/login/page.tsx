import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle} from "@/components/ui/card";
import {Label} from "@/components/ui/label";
import {Input} from "@/components/ui/input";
import {Button} from "@/components/ui/button";

const Login = () => {
    return (
        <main className="h-screen grid place-content-center">
            <Card className="w-[25rem]">
                <CardHeader>
                    <CardTitle>Sign In</CardTitle>
                    <CardDescription>Please enter your email and password</CardDescription>
                </CardHeader>
                <CardContent>
                    <form>
                        <div className="grid w-full items-center gap-4">
                            <div className="flex flex-col space-y-1.5">
                                <Label htmlFor="email">Your email</Label>
                                <Input id="email" placeholder="example@example.com" />
                            </div>
                            <div className="flex flex-col space-y-1.5 my-3">
                                <Label htmlFor="email">Your password</Label>
                                <Input type="password" id="email" placeholder="*********"/>
                            </div>
                            <div>
                                <Button type="submit" className="w-full">Sign In</Button>
                            </div>
                        </div>
                    </form>
                </CardContent>
                <CardFooter className="flex justify-between items-center">

                </CardFooter>
            </Card>
        </main>
    )
}

export default Login;
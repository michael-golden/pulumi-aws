// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Retrieve information about a Secrets Manager secret rotation. To retrieve secret metadata, see the [`aws.secretsmanager.Secret` data source](https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret.html). To retrieve a secret value, see the [`aws.secretsmanager.SecretVersion` data source](https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version.html).
 *
 * ## Example Usage
 * ### Retrieve Secret Rotation Configuration
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = aws.secretsmanager.getSecretRotation({
 *     secretId: data.aws_secretsmanager_secret.example.id,
 * });
 * ```
 */
export function getSecretRotation(args: GetSecretRotationArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretRotationResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("aws:secretsmanager/getSecretRotation:getSecretRotation", {
        "secretId": args.secretId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSecretRotation.
 */
export interface GetSecretRotationArgs {
    /**
     * Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
     */
    readonly secretId: string;
}

/**
 * A collection of values returned by getSecretRotation.
 */
export interface GetSecretRotationResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The ARN of the secret.
     */
    readonly rotationEnabled: boolean;
    /**
     * The decrypted part of the protected secret information that was originally provided as a string.
     */
    readonly rotationLambdaArn: string;
    /**
     * The decrypted part of the protected secret information that was originally provided as a binary. Base64 encoded.
     */
    readonly rotationRules: outputs.secretsmanager.GetSecretRotationRotationRule[];
    readonly secretId: string;
}
